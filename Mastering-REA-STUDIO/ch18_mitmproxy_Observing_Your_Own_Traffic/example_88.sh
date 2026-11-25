mitmdump --mode reverse:http://127.0.0.1:8800 \
  --listen-host 127.0.0.1 --listen-port 8801 \
  -s kettle_addon.py \
  -w ~/studio/captures/run2.mitm
