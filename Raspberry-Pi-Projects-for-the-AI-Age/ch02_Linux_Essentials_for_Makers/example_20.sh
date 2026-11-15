systemctl status ssh             # is the service running?
sudo systemctl start ssh         # start it now
sudo systemctl stop ssh          # stop it now
sudo systemctl restart ssh       # restart it
sudo systemctl enable ssh        # start at every boot
sudo systemctl disable ssh       # do not start at boot
journalctl -u ssh -n 50          # last 50 log lines
journalctl -u ssh -f             # follow the log live
