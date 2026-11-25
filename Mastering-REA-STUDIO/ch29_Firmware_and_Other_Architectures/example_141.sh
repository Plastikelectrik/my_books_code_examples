cd ~/studio/targets/kettle-fw
aarch64-linux-gnu-gcc -O1 -o rootfs/bin/kettle \
  ../kettle/src/kettle.c
file rootfs/bin/kettle
