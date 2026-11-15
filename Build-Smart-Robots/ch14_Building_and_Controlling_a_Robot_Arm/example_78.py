# Runs ON the ESP32. Servo signals on GPIO 13,12,14,27
from machine import Pin, PWM
import sys
import select

PINS = [13, 12, 14, 27]   # base, shoulder, elbow, grip
LIMITS = [(0, 180), (15, 165), (0, 150), (20, 90)]
servos = [PWM(Pin(p), freq=50) for p in PINS]

def set_angle(i, deg):
    lo, hi = LIMITS[i]
    deg = max(lo, min(hi, deg))
    # 0.5 ms .. 2.5 ms pulse within a 20 ms period
    us = 500 + deg * 2000 / 180
    servos[i].duty_ns(int(us * 1000))

for i, a in enumerate([90, 90, 90, 60]):
    set_angle(i, a)          # safe start pose

poll = select.poll()
poll.register(sys.stdin, select.POLLIN)
while True:
    if poll.poll(10):
        line = sys.stdin.readline().strip()
        if line.startswith("A,"):
            try:
                vals = [float(v) for v in
                        line[2:].split(",")]
                for i, a in enumerate(vals[:4]):
                    set_angle(i, a)
                print("OK")
            except ValueError:
                print("ERR")
