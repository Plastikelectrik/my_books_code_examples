python3 kettle_server.py &
mitmdump --mode reverse:http://127.0.0.1:8800 \
  --listen-host 127.0.0.1 --listen-port 8801 \
  -w ~/studio/captures/run1.mitm &
KETTLE_URL=http://127.0.0.1:8801/api/recipes \
  python3 kettle_client.py
