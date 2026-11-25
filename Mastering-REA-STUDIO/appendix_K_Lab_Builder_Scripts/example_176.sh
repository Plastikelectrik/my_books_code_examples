#!/usr/bin/env bash
set -euo pipefail
archive="$1"
expected="$2"
dest="$3"

actual=$(sha256sum "$archive" | cut -d' ' -f1)
if [ "$actual" != "$expected" ]; then
  echo "DIGEST MISMATCH for $archive" >&2
  echo "expected $expected" >&2
  echo "actual   $actual" >&2
  exit 1
fi
mkdir -p "$dest"
unzip -q "$archive" -d "$dest"
echo "installed $archive into $dest"
