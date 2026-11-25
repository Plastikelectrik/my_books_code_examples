#!/usr/bin/env bash
set -euo pipefail
T=~/studio/tools

python3 -m venv "$T/angr-env"
"$T/angr-env/bin/pip" install angr

python3 -m venv "$T/oracle-env"
"$T/oracle-env/bin/pip" install hypothesis pytest

python3 -m venv "$T/r2env"
"$T/r2env/bin/pip" install r2pipe rzpipe

python3 -m venv "$T/frida-env"
"$T/frida-env/bin/pip" install frida
echo "Environments ready in $T"
