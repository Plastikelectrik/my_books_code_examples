#!/usr/bin/env bash
set -euo pipefail
K=~/studio/targets/kettle
mkdir -p "$K/bin"
gcc -O1 -g -Wall -o "$K/bin/kettle" "$K/src/kettle.c"
cp "$K/bin/kettle" "$K/bin/kettle-stripped"
strip "$K/bin/kettle-stripped"
gcc -O2 -o "$K/bin/kettle-o2" "$K/src/kettle.c"
strip "$K/bin/kettle-o2"
aarch64-linux-gnu-gcc -O1 -o "$K/bin/kettle-arm64" \
  "$K/src/kettle.c"

L=~/studio/targets/kettle-lock
mkdir -p "$L"
gcc -O0 -o "$L/kettle-lock" "$L/src/kettle-lock.c"
sha256sum "$K"/bin/* "$L/kettle-lock"
