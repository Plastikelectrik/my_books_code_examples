G=/opt/ghidra_12.1.4_PUBLIC
J=/usr/lib/jvm/java-21-openjdk-amd64
echo "export GHIDRA_INSTALL_DIR=$G" >> ~/.bashrc
echo "export JAVA_HOME=$J" >> ~/.bashrc
source ~/.bashrc
"$GHIDRA_INSTALL_DIR/ghidraRun" &
