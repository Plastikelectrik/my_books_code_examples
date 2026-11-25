T=~/studio/targets/kettle/bin/kettle-stripped
rea function "$T" brew_time_addr --provider ghidra \
  --json > ev-ghidra.json
rea function "$T" brew_time_addr --provider ida \
  --json > ev-ida.json
