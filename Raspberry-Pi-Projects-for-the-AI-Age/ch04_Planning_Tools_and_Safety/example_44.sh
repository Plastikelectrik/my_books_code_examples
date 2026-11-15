#!/bin/bash
# Archive project files and settings with a date
set -e
DEST="/media/backup/$(hostname)"
STAMP=$(date +%Y-%m-%d_%H%M)
mkdir -p "$DEST"
sudo tar -czf "$DEST/config_$STAMP.tar.gz" \
    /boot/firmware/config.txt \
    /etc/systemd/system/*.service \
    /home/oscar/projects \
    2>/dev/null
# keep only the 10 newest archives
ls -1t "$DEST"/config_*.tar.gz | tail -n +11 | xargs -r rm
echo "Backup written to $DEST/config_$STAMP.tar.gz"
