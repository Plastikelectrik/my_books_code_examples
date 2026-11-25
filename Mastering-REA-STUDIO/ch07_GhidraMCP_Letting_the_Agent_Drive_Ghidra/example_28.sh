git clone https://github.com/LaurieWired/GhidraMCP
cd GhidraMCP/extension
git checkout TAG
"$GHIDRA_INSTALL_DIR/support/gradle/gradlew" \
  buildExtension
ls dist
