mkdir -p rootfs/etc rootfs/data
printf 'model=KT-100\nserver=127.0.0.1\n' \
  > rootfs/etc/kettle.conf
cp ../ktl/sample.ktl rootfs/data/
mksquashfs rootfs rootfs.sqsh -comp xz -noappend
