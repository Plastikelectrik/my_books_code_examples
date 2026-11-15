import json
import socket
import threading
import time

PORT = 5005

def fake_robot(n=20):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for i in range(n):
        msg = {"seq": i, "dist": 60 - i * 2.0,
               "batt": round(7.8 - i * 0.01, 2)}
        s.sendto(json.dumps(msg).encode(),
                 ("127.0.0.1", PORT))
        time.sleep(0.05)

rx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
rx.bind(("0.0.0.0", PORT))
rx.settimeout(1.0)
threading.Thread(target=fake_robot, daemon=True).start()

received, last_seq = 0, -1
while True:
    try:
        data, addr = rx.recvfrom(1024)
    except socket.timeout:
        break                       # robot went quiet
    msg = json.loads(data)
    if msg["seq"] != last_seq + 1:
        print("lost packets before", msg["seq"])
    last_seq = msg["seq"]
    received += 1
    if msg["dist"] < 30:
        print(f"WARNING: obstacle {msg['dist']} cm")
print(f"received {received} messages, "
      f"last battery {msg['batt']} V")
