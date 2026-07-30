#!/usr/bin/env bash
set -euo pipefail

# Release source and digest are repository-owned review inputs. The digest is
# the SHA-256 recorded by the upstream GitHub release metadata and was also
# verified against the downloaded archive before this file was committed.
readonly LYCHEE_VERSION="0.24.2"
readonly LYCHEE_TARGET="x86_64-unknown-linux-gnu"
readonly LYCHEE_ARCHIVE="lychee-${LYCHEE_TARGET}.tar.gz"
readonly LYCHEE_RELEASE_URL="https://github.com/lycheeverse/lychee/releases/download/lychee-v${LYCHEE_VERSION}/${LYCHEE_ARCHIVE}"
readonly LYCHEE_ARCHIVE_SHA256="1f4e0ef7f6554a6ed33dd7ac144fb2e1bbed98598e7af973042fc5cd43951c9a"
readonly LYCHEE_MEMBER="lychee-${LYCHEE_TARGET}/lychee"

if [[ $# -ne 1 || "$1" != /* ]]; then
  echo "usage: $0 /absolute/install/directory" >&2
  exit 2
fi

if [[ "$(uname -s)" != "Linux" || "$(uname -m)" != "x86_64" ]]; then
  echo "verified Lychee installer supports only Linux x86_64" >&2
  exit 2
fi

readonly install_dir="$1"
readonly temporary_root="${RUNNER_TEMP:-/tmp}"
work_dir="$(mktemp -d "${temporary_root%/}/verified-lychee.XXXXXX")"
readonly work_dir
trap 'rm -rf -- "${work_dir:?}"' EXIT

archive_path="${work_dir}/${LYCHEE_ARCHIVE}"
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
  "${LYCHEE_RELEASE_URL}"

printf '%s  %s\n' "${LYCHEE_ARCHIVE_SHA256}" "${archive_path}" \
  | sha256sum --check --strict

mapfile -t member_listing < <(
  tar --list --verbose --gzip --file "${archive_path}" "${LYCHEE_MEMBER}"
)
if [[ ${#member_listing[@]} -ne 1 ]]; then
  echo "verified archive does not contain exactly one ${LYCHEE_MEMBER}" >&2
  exit 1
fi
if [[ "${member_listing[0]:0:1}" != "-" ]]; then
  echo "verified archive does not contain exactly one regular ${LYCHEE_MEMBER}" >&2
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
  "${LYCHEE_MEMBER}"

if [[ ! -f "${extract_dir}/lychee" || -L "${extract_dir}/lychee" ]]; then
  echo "verified archive did not produce the expected regular Lychee binary" >&2
  exit 1
fi

install -d -m 0755 "${install_dir}"
install -m 0755 "${extract_dir}/lychee" "${install_dir}/lychee"

version_output="$(
  env -i PATH="/usr/local/bin:/usr/bin:/bin" \
    "${install_dir}/lychee" --version
)"
readonly version_output
if [[ "${version_output}" != "lychee ${LYCHEE_VERSION}"* ]]; then
  echo "unexpected Lychee version: ${version_output}" >&2
  exit 1
fi

echo "Installed verified ${version_output}."
