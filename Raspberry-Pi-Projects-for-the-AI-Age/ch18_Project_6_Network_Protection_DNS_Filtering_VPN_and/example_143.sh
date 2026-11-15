echo "net.ipv4.ip_forward=1" | \
     sudo tee /etc/sysctl.d/99-wireguard.conf
sudo sysctl --system
sudo ufw allow 51820/udp comment "WireGuard"
sudo ufw route allow in on wg0 out on eth0
sudo ufw allow in on wg0 to any port 53 \
     comment "DNS via VPN"
