# Run on the Raspberry Pi
import csv
import time
import serial

link = serial.Serial("/dev/ttyACM0", 115200,
                     timeout=0.2)
time.sleep(2)
t0 = time.monotonic()

with open("sensor_log.csv", "w", newline="") as f:
    out = csv.writer(f)
    out.writerow(["time_s", "type", "value"])
    while time.monotonic() - t0 < 30:   # 30 s
        raw = link.readline()
        line = raw.decode("ascii", "ignore").strip()
        if "," not in line:
            continue
        kind, value = line.split(",", 1)
        t = round(time.monotonic() - t0, 3)
        out.writerow([t, kind, value])
print("saved sensor_log.csv")
