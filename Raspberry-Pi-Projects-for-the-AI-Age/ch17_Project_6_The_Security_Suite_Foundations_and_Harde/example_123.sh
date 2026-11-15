sudo sshd -t  # syntax check, no output = ok
sudo systemctl restart ssh
# in a NEW terminal on your computer:
ssh oscar@guardian.local
