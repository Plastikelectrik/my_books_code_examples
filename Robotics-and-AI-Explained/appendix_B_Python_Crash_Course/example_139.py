import math

def distance(x1, y1, x2=0.0, y2=0.0):
    """Straight-line distance between two points."""
    return math.hypot(x2 - x1, y2 - y1)

def wheel_distance(ticks, ticks_per_rev=360,
                   diameter_m=0.065):
    return ticks / ticks_per_rev * math.pi * diameter_m

print(f"{distance(3, 4):.2f}")
print(f"{distance(1, 1, 4, 5):.2f}")
print(f"{wheel_distance(720):.3f} m")
