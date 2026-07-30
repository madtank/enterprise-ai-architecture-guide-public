#!/usr/bin/env bash
set -euo pipefail

readonly UV_VERSION="0.11.15"
readonly LOCK_CUTOFF="2026-07-28T19:01:14Z"
readonly LOCK_COMMAND="uv --no-config --no-python-downloads pip compile requirements.in --universal --generate-hashes --python-version 3.11 --exclude-newer ${LOCK_CUTOFF} --upgrade --only-binary :all: --no-sources --no-cache --default-index https://pypi.org/simple --output-file requirements.txt"

root_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
readonly root_dir
cd "${root_dir}"

version_output="$(uv --version)"
readonly version_output
if [[ "${version_output}" != "uv ${UV_VERSION}"* ]]; then
  echo "requirements lock requires uv ${UV_VERSION}; found ${version_output}" >&2
  exit 1
fi

readonly temporary_root="${RUNNER_TEMP:-/tmp}"
generated_lock="$(mktemp "${temporary_root%/}/requirements.generated.XXXXXX.txt")"
readonly generated_lock
trap 'rm -f -- "${generated_lock:?}"' EXIT

uv --no-config --no-python-downloads --quiet pip compile requirements.in \
  --universal \
  --generate-hashes \
  --python-version 3.11 \
  --exclude-newer "${LOCK_CUTOFF}" \
  --upgrade \
  --only-binary :all: \
  --no-sources \
  --no-cache \
  --default-index https://pypi.org/simple \
  --custom-compile-command "${LOCK_COMMAND}" \
  --output-file "${generated_lock}"

python3 scripts/check_requirements_lock.py --generated "${generated_lock}"
