import math

def wrap(angle_rad):
    return math.atan2(math.sin(angle_rad),
                      math.cos(angle_rad))

current, target = math.radians(359), math.radians(1)
naive = math.degrees(target - current)
smart = math.degrees(wrap(target - current))
print(f"naive turn: {naive:7.1f} degrees")
print(f"wrapped   : {smart:7.1f} degrees")
