export GHIDRA_INSTALL_DIR=/opt/ghidra_12.1.4_PUBLIC
ghidra-mcp --headless \
  --binary ~/studio/targets/kettle/bin/kettle-stripped \
  --project ~/studio/evidence/kettle/ghidra-mcp
