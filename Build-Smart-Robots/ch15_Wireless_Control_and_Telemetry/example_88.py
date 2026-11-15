# Runs on the Raspberry Pi with rover.py
import threading
import time
from rover import Rover

L = 0.15                         # wheelbase (m)

def control_loop(state):
    bot = Rover()
    try:
        while True:
            ticks, dist, age = bot.status()
            state["dist"] = round(dist, 1)
            fresh = time.time() - state["updated"] < 1.0
            v = state["v"] if fresh else 0.0
            w = state["w"] if fresh else 0.0
            bot.velocity(v - w * L / 2, v + w * L / 2)
            time.sleep(0.05)
    finally:
        bot.close()

# In dashboard.py, before app.run(...):
# threading.Thread(target=control_loop,
#                  args=(state,), daemon=True).start()
