cd ~/studio/evidence/kettle-fw/extract
K=$(find . -path '*bin/kettle' | head -n 1)
qemu-aarch64 -L /usr/aarch64-linux-gnu "$K" green 4
