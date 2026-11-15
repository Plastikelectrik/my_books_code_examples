sudo apt install -y mosquitto mosquitto-clients
sudo ufw allow from 192.168.1.0/24 to any port 1883 \
     comment "MQTT from home"
mosquitto_sub -h localhost -t "frigate/#" -v
