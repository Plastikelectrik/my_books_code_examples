sudo systemctl daemon-reload  # read the new unit file
sudo systemctl enable --now health    # enable and start
systemctl status health
journalctl -u health -f               # watch the log
