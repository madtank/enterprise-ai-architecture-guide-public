#!/usr/bin/env python3
"""Fail closed on external-reference URLs before the network link checker runs."""

from __future__ import annotations

import argparse
import ipaddress
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit


ALLOWED_HOSTS = frozenset(
    {
        "adk.dev",
        "agentskills.io",
        "airc.nist.gov",
        "arxiv.org",
        "atlas.mitre.org",
        "aws.amazon.com",
        "azure.microsoft.com",
        "cloud.google.com",
        "cloudsecurityalliance.org",
        "code.claude.com",
        "csrc.nist.gov",
        "developers.openai.com",
        "digital-strategy.ec.europa.eu",
        "docs.aws.amazon.com",
        "docs.astral.sh",
        "docs.cloud.google.com",
        "docs.github.com",
        "docs.gitlab.com",
        "doi.org",
        "dora.dev",
        "eur-lex.europa.eu",
        "genai.owasp.org",
        "github.blog",
        "github.com",
        "learn.chatgpt.com",
        "learn.microsoft.com",
        "modelcontextprotocol.io",
        "oecd.ai",
        "openai.com",
        "pypi.org",
        "slsa.dev",
        "sre.google",
        "www.anthropic.com",
        "www.cisa.gov",
        "www.coe.int",
        "www.cyber.gov.au",
        "www.etsi.org",
        "www.iso.org",
        "www.ncsc.gov.uk",
        "www.nist.gov",
        "www.nsa.gov",
        "www.ntia.gov",
    }
)

URL_PATTERN = re.compile(r"https?://[^\s<>\"']+", re.IGNORECASE)


def normalize_extracted_url(raw_url: str) -> str:
    """Remove Markdown punctuation without rewriting the authority."""
    url = raw_url
    url = url.rstrip(".,;:!?")
    while url.endswith(")") and url.count(")") > url.count("("):
        url = url[:-1]
    return url.rstrip(".,;:!?")


def validate_url(url: str) -> list[str]:
    """Return policy violations for one URL."""
    violations: list[str] = []
    if "\\" in url:
        return ["backslashes are prohibited in external URLs"]

    try:
        parsed = urlsplit(url)
        port = parsed.port
    except ValueError as exc:
        return [f"invalid URL: {exc}"]

    if parsed.scheme != "https":
        violations.append("scheme must be https")
    if parsed.username is not None or parsed.password is not None:
        violations.append("userinfo is prohibited")
    if port not in (None, 443):
        violations.append("port must be 443 or omitted")

    host = parsed.hostname
    if not host:
        violations.append("hostname is required")
        return violations
    if host.endswith("."):
        violations.append("trailing-dot hostnames are prohibited")
        return violations

    try:
        normalized_host = host.encode("idna").decode("ascii").lower()
    except UnicodeError:
        violations.append("hostname is not valid IDNA")
        return violations

    try:
        ipaddress.ip_address(normalized_host)
    except ValueError:
        pass
    else:
        violations.append("IP-literal destinations are prohibited")

    if normalized_host not in ALLOWED_HOSTS:
        violations.append(f"hostname is not allowlisted: {normalized_host}")

    return violations


def iter_urls(path: Path):
    """Yield line-numbered HTTP(S) URLs found in a Markdown source."""
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        for match in URL_PATTERN.finditer(line):
            yield line_number, normalize_extracted_url(match.group(0))


def check_paths(paths: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in paths:
        if not path.is_file():
            errors.append(f"{path}: file does not exist")
            continue
        for line_number, url in iter_urls(path):
            for violation in validate_url(url):
                errors.append(f"{path}:{line_number}: {violation}: {url}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Require HTTPS URLs on the approved authoritative-source host list."
    )
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()

    errors = check_paths(args.paths)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    print(f"Validated external-reference URL policy for {len(args.paths)} files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
