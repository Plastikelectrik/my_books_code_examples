T=./kettle-stripped
sha256sum "$T" > ~/studio/captures/kettle-run1.txt
python3 run_frida.py watch_strcmp.js "$T" black \
  >> ~/studio/captures/kettle-run1.txt 2>&1
