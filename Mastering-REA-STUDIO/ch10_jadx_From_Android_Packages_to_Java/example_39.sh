cd ~/studio/tools
sha256sum jadx-*.zip
mkdir -p jadx && unzip -q jadx-*.zip -d jadx
echo 'export PATH="$HOME/studio/tools/jadx/bin:$PATH"' \
  >> ~/.bashrc
source ~/.bashrc && jadx --version
