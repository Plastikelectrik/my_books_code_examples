lsblk  # find the card, e.g. /dev/sdb
sudo dd if=/dev/sdb of=arcade.img bs=4M status=progress
