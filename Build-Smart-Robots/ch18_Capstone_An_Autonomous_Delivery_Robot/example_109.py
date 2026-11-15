# Runs on the Raspberry Pi with rover.py, odometry.py
# and delivery_sim.py (for the planning functions)
import math
import time
from rover import Rover
from odometry import Odometry
from delivery_sim import (make_room, inflate, plan,
                          pure_pursuit, prune, cell,
                          STATIONS)

L = 0.154                       # calibrated wheelbase
bot = Rover()
odo = Odometry(0.000578, L)
seen = make_room()              # your measured room
known = inflate(seen)

def drive_to(name):
    global seen, known
    goal = STATIONS[name]
    x, y, th = odo.pose()
    path = plan(known, (x, y), goal)
    if path is None:
        return "no path"
    while True:
        (tl, tr), dist, age = bot.status()
        if age > 0.5:
            bot.stop()
            return "no data from firmware"
        x, y, th = odo.update(tl, tr)
        if math.dist((x, y), goal) < 0.08:
            bot.stop()
            return "arrived"
        if 0 < dist < 35:       # something ahead
            d = dist / 100 + 0.05
            ox = x + d * math.cos(th)
            oy = y + d * math.sin(th)
            r, c = cell(ox, oy)
            if not seen[r, c]:
                seen[r, c] = 1
                known = inflate(seen)
                bot.stop()
                path = plan(known, (x, y), goal)
                if path is None:
                    return "blocked"
        prune(path, (x, y, th))
        v, w = pure_pursuit((x, y, th), path, v=0.15)
        bot.velocity(v - w * L / 2, v + w * L / 2)
        time.sleep(0.05)

try:
    for stop in ["kitchen", "office", "home"]:
        result = drive_to(stop)
        print(stop, "->", result)
        if result != "arrived":
            break
        time.sleep(10)          # loading / unloading
finally:
    bot.close()
