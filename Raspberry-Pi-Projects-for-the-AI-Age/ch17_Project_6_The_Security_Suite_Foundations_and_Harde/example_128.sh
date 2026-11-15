sudo cscli decisions add --ip 203.0.113.50 \
     --duration 5m --reason "test"
sudo cscli decisions list
sudo cscli decisions delete --ip 203.0.113.50
