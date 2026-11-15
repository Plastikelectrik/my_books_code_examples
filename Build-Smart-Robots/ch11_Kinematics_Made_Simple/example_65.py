# Runs on the Raspberry Pi with rover.py
import math
import time
from rover import Rover
from odometry import Odometry   # previous example

bot = Rover()
odo = Odometry(m_per_tick=0.000578, wheelbase=0.15)
try:
    t_end = time.monotonic() + 6
    while time.monotonic() < t_end:
        (tl, tr), dist, age = bot.status()
        x, y, th = odo.update(tl, tr)
        bot.velocity(0.10, 0.14)      # gentle left arc
        print(f"x={x:.2f} y={y:.2f} "
              f"th={math.degrees(th):.0f}")
        time.sleep(0.05)
finally:
    bot.close()
