"$GHIDRA_INSTALL_DIR/support/analyzeHeadless" \
  /tmp/ghidra-tmp kettle-quick \
  -import ~/studio/targets/kettle/bin/kettle-stripped \
  -scriptPath ~/studio/scripts/ghidra \
  -postScript ListFunctions.java \
  -deleteProject
