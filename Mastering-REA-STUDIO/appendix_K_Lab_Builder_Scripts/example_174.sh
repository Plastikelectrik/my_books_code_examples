#!/usr/bin/env bash
set -euo pipefail

sudo apt update
sudo apt install -y build-essential git curl unzip \
  zip python3 python3-venv pipx procps file \
  binutils gdb openjdk-21-jdk squashfs-tools \
  meson ninja-build gcc-aarch64-linux-gnu qemu-user
pipx ensurepath
pipx install uv
pipx install frida-tools
pipx install mitmproxy

mkdir -p ~/studio/{targets,evidence,captures}
mkdir -p ~/studio/{specs,rebuild,oracles}
mkdir -p ~/studio/{notes,tools,scripts}
echo "Base setup finished. Now install Node.js,"
echo "Ghidra, jadx, Apktool, ImHex and radare2"
echo "from their official sources (Appendix I)."
