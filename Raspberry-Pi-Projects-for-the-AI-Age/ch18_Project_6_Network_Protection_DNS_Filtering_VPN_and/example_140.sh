sudo apt install -y wireguard iptables qrencode
sudo -i                     # become root for this part
cd /etc/wireguard
umask 077                   # new files: owner only
wg genkey | tee server.key | wg pubkey > server.pub
cat server.pub
