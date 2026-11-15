# Runs on the Raspberry Pi, next to rover.py
import time
from rover import Rover

bot = Rover()
try:
    while True:
        ticks, dist, age = bot.status()
        if age > 0.5:
            print("no data from Arduino!")
            bot.stop()
        elif 0 < dist < 30:
            print(f"obstacle at {dist:.0f} cm: stop")
            bot.stop()
            break
        else:
            bot.velocity(0.15, 0.15)   # 15 cm/s
        time.sleep(0.05)               # 20 Hz
finally:
    bot.close()
