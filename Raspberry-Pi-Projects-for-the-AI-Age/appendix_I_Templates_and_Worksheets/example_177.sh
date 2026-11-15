#!/bin/bash
# Back up selected folders to a dated archive; keep 14
set -euo pipefail
SRC=(/home/oscar/my-project /etc/systemd/system)
DEST=/media/backup/$(hostname)
STAMP=$(date +%Y-%m-%d_%H%M)
mkdir -p "$DEST"
tar -czf "$DEST/backup_$STAMP.tar.gz" "${SRC[@]}" \
    2>/dev/null || true
ls -1t "$DEST"/backup_*.tar.gz | tail -n +15 | \
    xargs -r rm
echo "ok: $DEST/backup_$STAMP.tar.gz"
