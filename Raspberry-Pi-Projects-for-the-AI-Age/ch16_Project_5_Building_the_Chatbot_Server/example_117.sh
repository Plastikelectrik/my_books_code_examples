cd ~/chatbot
openssl req -x509 -newkey rsa:2048 -nodes -days 825 \
  -keyout key.pem -out cert.pem \
  -subj "/CN=chatbot.local"
chmod 600 key.pem
