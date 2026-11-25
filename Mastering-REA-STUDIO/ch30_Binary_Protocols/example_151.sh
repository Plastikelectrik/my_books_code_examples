python3 kb_server.py &
mitmdump --mode reverse:tcp://127.0.0.1:8900 \
  --listen-host 127.0.0.1 --listen-port 8901 \
  -s kb_record.py &
