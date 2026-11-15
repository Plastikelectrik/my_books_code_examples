sudo apt install -y crowdsec
sudo apt install -y crowdsec-firewall-bouncer-nftables
sudo cscli collections list        # installed detections
sudo cscli metrics                 # what it has read
sudo cscli decisions list          # current blocks
