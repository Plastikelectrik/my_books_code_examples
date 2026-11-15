# Convert encoder ticks into distance traveled
import math

TICKS_PER_REV = 360        # ticks for one full turn
WHEEL_DIAMETER = 0.065     # meters (65 mm wheel)
circumference = math.pi * WHEEL_DIAMETER

def ticks_to_meters(ticks):
    return ticks / TICKS_PER_REV * circumference

for ticks in [90, 360, 1000, 5000]:
    d = ticks_to_meters(ticks)
    print(f"{ticks:5d} ticks = {d:.3f} m")
