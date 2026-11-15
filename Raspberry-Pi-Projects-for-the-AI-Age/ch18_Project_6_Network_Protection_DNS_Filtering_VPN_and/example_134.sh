sudo ufw allow from 192.168.1.0/24 to any port 53 \
     comment "DNS from home"
sudo ufw allow from 192.168.1.0/24 to any port 80,443 \
     proto tcp comment "Pi-hole web from home"
