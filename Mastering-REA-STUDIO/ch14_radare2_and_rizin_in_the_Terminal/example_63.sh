cd ~/studio/tools
git clone https://github.com/radareorg/radare2
cd radare2
git checkout "$(git describe --tags --abbrev=0)"
sys/install.sh
r2 -v
