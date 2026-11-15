# Runs ON the ESP32. Put your Wi-Fi data in secrets.py
import network
import socket
import time
import json
from secrets import SSID, PASSWORD, TARGET_IP

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)
for _ in range(40):
    if wlan.isconnected():
        break
    time.sleep(0.25)
print("IP address:", wlan.ifconfig()[0])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
PORT = 5005
t0 = time.ticks_ms()
while True:
    t = time.ticks_diff(time.ticks_ms(), t0) / 1000
    msg = {"t": round(t, 2), "dist": 54.2,
           "batt": 7.6}            # replace with sensors
    sock.sendto(json.dumps(msg).encode(),
                (TARGET_IP, PORT))
    time.sleep(0.1)                # 10 Hz
