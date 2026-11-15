#!/bin/bash
# Mount the share first, for example:
#   sudo mount -t cifs //batocera.local/share \
#        /mnt/batocera -o guest,uid=$(id -u)
set -e
SRC=/mnt/batocera
DEST=~/backups/batocera/$(date +%Y-%m-%d)
mkdir -p "$DEST"
rsync -a "$SRC/saves/" "$DEST/saves/"
rsync -a "$SRC/system/" "$DEST/system/"
echo "Saves copied to $DEST"
