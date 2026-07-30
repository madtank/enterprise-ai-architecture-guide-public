#!/usr/bin/env python3
"""Validate the repository's Python lock policy and resolver reproduction."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


class LockPolicyError(ValueError):
    """Raised when a dependency declaration violates repository policy."""


NAME_RE = r"[A-Za-z0-9][A-Za-z0-9._-]*"
PIN_RE = re.compile(rf"^({NAME_RE})==([^\s;\\]+)$")
LOCK_PIN_RE = re.compile(rf"^({NAME_RE})==([^\s;\\]+)(?:\s+\\)?$")
HASH_RE = re.compile(r"^\s*--hash=sha256:[0-9a-f]{64}(?:\s+\\)?$")
FORBIDDEN_PREFIXES = (
    "-e ",
    "--editable ",
    "-f ",
    "--find-links ",
    "-i ",
    "--index-url ",
    "--extra-index-url ",
    "--trusted-host ",
)
REQUIRED_HEADER_FRAGMENTS = (
    "uv --no-config --no-python-downloads pip compile requirements.in",
    "--universal",
    "--generate-hashes",
    "--exclude-newer",
    "--upgrade",
    "--only-binary :all:",
    "--no-sources",
    "--no-cache",
    "--default-index https://pypi.org/simple",
)


def canonical_name(name: str) -> str:
    """Apply the package-name normalization used by Python packaging tools."""

    return re.sub(r"[-_.]+", "-", name).lower()


def read_direct_pins(path: Path) -> dict[str, str]:
    """Read exact direct requirements from requirements.in."""

    pins: dict[str, str] = {}
    for line_number, raw_line in enumerate(path.read_text().splitlines(), 1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("-") or "@" in line:
            raise LockPolicyError(
                f"{path}:{line_number}: options, URLs, and local sources are prohibited"
            )
        match = PIN_RE.fullmatch(line)
        if not match:
            raise LockPolicyError(
                f"{path}:{line_number}: direct dependencies must use name==version"
            )
        name, version = match.groups()
        normalized = canonical_name(name)
        if normalized in pins:
            raise LockPolicyError(
                f"{path}:{line_number}: duplicate direct dependency {name}"
            )
        pins[normalized] = version
    if not pins:
        raise LockPolicyError(f"{path}: no direct dependencies found")
    return pins


def read_locked_pins(path: Path) -> dict[str, tuple[str, int]]:
    """Read exact locked requirements and require a SHA-256 for every package."""

    text = path.read_text()
    header = "\n".join(text.splitlines()[:5])
    for fragment in REQUIRED_HEADER_FRAGMENTS:
        if fragment not in header:
            raise LockPolicyError(
                f"{path}: generated header is missing required fragment {fragment!r}"
            )

    locked: dict[str, tuple[str, int]] = {}
    current_name: str | None = None
    current_line = 0
    current_hashes = 0

    def finish_current() -> None:
        if current_name is not None and current_hashes == 0:
            raise LockPolicyError(
                f"{path}:{current_line}: locked package {current_name} has no SHA-256"
            )

    for line_number, raw_line in enumerate(text.splitlines(), 1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith(FORBIDDEN_PREFIXES) or "@" in line:
            raise LockPolicyError(
                f"{path}:{line_number}: indexes, URLs, editable, and local sources are prohibited"
            )
        pin_match = LOCK_PIN_RE.fullmatch(line)
        if pin_match:
            finish_current()
            name, version = pin_match.groups()
            normalized = canonical_name(name)
            if normalized in locked:
                raise LockPolicyError(
                    f"{path}:{line_number}: duplicate locked dependency {name}"
                )
            locked[normalized] = (version, line_number)
            current_name = normalized
            current_line = line_number
            current_hashes = 0
            continue
        if HASH_RE.fullmatch(raw_line):
            if current_name is None:
                raise LockPolicyError(
                    f"{path}:{line_number}: SHA-256 appears before a locked package"
                )
            current_hashes += 1
            continue
        raise LockPolicyError(
            f"{path}:{line_number}: unexpected lock content {line!r}"
        )

    finish_current()
    if not locked:
        raise LockPolicyError(f"{path}: no locked dependencies found")
    return locked


def validate_lock(input_path: Path, lock_path: Path) -> tuple[int, int]:
    """Validate lock syntax, hashes, and direct-pin correspondence.

    Completeness is established separately by reproducing the lock with the
    pinned resolver and comparing the full files.
    """

    direct = read_direct_pins(input_path)
    locked = read_locked_pins(lock_path)
    for name, version in direct.items():
        locked_entry = locked.get(name)
        if locked_entry is None:
            raise LockPolicyError(
                f"{lock_path}: direct dependency {name} is absent from the lock"
            )
        locked_version, line_number = locked_entry
        if locked_version != version:
            raise LockPolicyError(
                f"{lock_path}:{line_number}: {name} is locked at {locked_version}, "
                f"but {input_path} requires {version}"
            )
    return len(direct), len(locked)


def compare_generated_lock(committed_path: Path, generated_path: Path) -> None:
    """Require the committed lock to match the resolver output byte for byte."""

    if committed_path.read_bytes() != generated_path.read_bytes():
        raise LockPolicyError(
            f"{committed_path}: content differs from pinned-resolver output "
            f"{generated_path}; regenerate and review the complete lock"
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate dependency lock policy and optional reproduction."
    )
    parser.add_argument(
        "--generated",
        type=Path,
        help="resolver-generated lock that must exactly match requirements.txt",
    )
    return parser.parse_args()


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    args = parse_args()
    try:
        direct_count, locked_count = validate_lock(
            root / "requirements.in", root / "requirements.txt"
        )
        if args.generated is not None:
            compare_generated_lock(root / "requirements.txt", args.generated)
    except (OSError, LockPolicyError) as error:
        print(f"Dependency lock validation failed: {error}", file=sys.stderr)
        return 1
    print(
        f"Validated {locked_count} hash-locked packages "
        f"for {direct_count} direct dependency."
    )
    if args.generated is not None:
        print("Committed lock matches the pinned-resolver output byte for byte.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
