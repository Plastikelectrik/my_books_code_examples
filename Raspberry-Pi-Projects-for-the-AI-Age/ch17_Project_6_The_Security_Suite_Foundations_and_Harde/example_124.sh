sudo apt install -y ufw
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow from 192.168.1.0/24 to any port 22 \
     proto tcp comment "SSH from home only"
sudo ufw enable
sudo ufw status verbose
