claude mcp add rea \
  -e GHIDRA_INSTALL_DIR=/opt/ghidra_12.1.4_PUBLIC \
  -e JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64 \
  -e REA_ANALYSIS_PROVIDER=ghidra \
  -- rea mcp
claude mcp list
