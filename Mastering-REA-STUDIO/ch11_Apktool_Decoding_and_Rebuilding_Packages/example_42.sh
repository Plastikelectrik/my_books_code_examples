mkdir -p ~/studio/tools/apktool && cd "$_"
sha256sum apktool_*.jar
mv apktool_*.jar apktool.jar
chmod +x apktool
sudo ln -sf "$PWD/apktool" /usr/local/bin/apktool
sudo ln -sf "$PWD/apktool.jar" /usr/local/bin/apktool.jar
apktool --version
