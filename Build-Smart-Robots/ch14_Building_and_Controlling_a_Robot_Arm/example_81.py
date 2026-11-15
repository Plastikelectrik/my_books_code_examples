# Runs on the computer connected to the arm's ESP32
import time
import serial
import numpy as np

arm = serial.Serial("/dev/ttyUSB0", 115200,
                    timeout=0.2)
time.sleep(1)

def send(pose, grip):
    b, s, e = pose
    arm.write(f"A,{b:.1f},{s:.1f},{e:.1f},{grip}\n"
              .encode())

def move(a, b, T, grip=60):
    a, b = np.array(a, float), np.array(b, float)
    n = max(2, int(T * 50))
    for tau in np.linspace(0, 1, n):
        s = 10 * tau**3 - 15 * tau**4 + 6 * tau**5
        send(a + (b - a) * s, grip)
        time.sleep(0.02)

home = [90, 90, 90]
above = [120, 70, 130]
move(home, above, 1.5)
move(above, home, 1.5)
arm.close()
