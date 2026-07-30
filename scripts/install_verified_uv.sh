#!/usr/bin/env bash
set -euo pipefail

# Release source and digest are repository-owned review inputs. The digest
# matches the checksum published with the upstream release and an independent
# download performed before this file was committed.
readonly UV_VERSION="0.11.15"
readonly UV_TARGET="x86_64-unknown-linux-gnu"
readonly UV_ARCHIVE="uv-${UV_TARGET}.tar.gz"
readonly UV_RELEASE_URL="https://github.com/astral-sh/uv/releases/download/${UV_VERSION}/${UV_ARCHIVE}"
readonly UV_ARCHIVE_SHA256="b03e572f010bea94a4a52d42671ba72981e12894f71576181a1d26ff68546da7"
readonly UV_MEMBER="uv-${UV_TARGET}/uv"

if [[ $# -ne 1 || "$1" != /* ]]; then
  echo "usage: $0 /absolute/install/directory" >&2
  exit 2
fi

if [[ "$(uname -s)" != "Linux" || "$(uname -m)" != "x86_64" ]]; then
  echo "verified uv installer supports only Linux x86_64" >&2
  exit 2
fi

readonly install_dir="$1"
readonly temporary_root="${RUNNER_TEMP:-/tmp}"
work_dir="$(mktemp -d "${temporary_root%/}/verified-uv.XXXXXX")"
readonly work_dir
trap 'rm -rf -- "${work_dir:?}"' EXIT

archive_path="${work_dir}/${UV_ARCHIVE}"
readonly archive_path

curl \
  --disable \
  --proto '=https' \
  --proto-redir '=https' \
  --tlsv1.2 \
  --fail \
  --location \
  --silent \
  --show-error \
  --retry 3 \
  --retry-all-errors \
  --connect-timeout 10 \
  --max-time 120 \
  --max-filesize 50000000 \
  --output "${archive_path}" \
  "${UV_RELEASE_URL}"

printf '%s  %s\n' "${UV_ARCHIVE_SHA256}" "${archive_path}" \
  | sha256sum --check --strict

mapfile -t member_listing < <(
  tar --list --verbose --gzip --file "${archive_path}" "${UV_MEMBER}"
)
if [[ ${#member_listing[@]} -ne 1 ]]; then
  echo "verified archive does not contain exactly one ${UV_MEMBER}" >&2
  exit 1
fi
if [[ "${member_listing[0]:0:1}" != "-" ]]; then
  echo "verified archive does not contain exactly one regular ${UV_MEMBER}" >&2
  exit 1
fi

extract_dir="${work_dir}/extract"
readonly extract_dir
mkdir -p "${extract_dir}"
tar \
  --extract \
  --gzip \
  --file "${archive_path}" \
  --directory "${extract_dir}" \
  --strip-components=1 \
  --no-same-owner \
  --no-same-permissions \
  "${UV_MEMBER}"

if [[ ! -f "${extract_dir}/uv" || -L "${extract_dir}/uv" ]]; then
  echo "verified archive did not produce the expected regular uv binary" >&2
  exit 1
fi

install -d -m 0755 "${install_dir}"
install -m 0755 "${extract_dir}/uv" "${install_dir}/uv"

version_output="$(
  env -i PATH="/usr/local/bin:/usr/bin:/bin" \
    "${install_dir}/uv" --version
)"
readonly version_output
if [[ "${version_output}" != "uv ${UV_VERSION}"* ]]; then
  echo "unexpected uv version: ${version_output}" >&2
  exit 1
fi

echo "Installed verified ${version_output}."
