import math

TICKS_PER_REV = 360
WHEEL_DIAMETER_M = 0.066
M_PER_TICK = math.pi * WHEEL_DIAMETER_M / TICKS_PER_REV

def ticks_to_m(ticks):
    return ticks * M_PER_TICK

# Two readings 0.1 s apart
t0, t1 = 1200, 1374
dt = 0.1
dist = ticks_to_m(t1 - t0)
print(f"meters per tick: {M_PER_TICK:.6f}")
print(f"moved {dist*100:.1f} cm in {dt} s")
print(f"speed {dist/dt:.3f} m/s")
