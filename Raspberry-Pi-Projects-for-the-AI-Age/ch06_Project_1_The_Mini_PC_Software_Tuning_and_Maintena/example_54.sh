#!/bin/bash
# Install a recommended set of open-source desktop apps
set -e
APPS=(
  firefox libreoffice thunderbird keepassxc
  gimp inkscape vlc thonny geany xournalpp
  htop gparted deja-dup
)
sudo apt update
sudo apt install -y "${APPS[@]}"
echo "Installed: ${APPS[*]}"
