# Slow down as the robot enters closer zones
def zone(d):
    if d < 0.45: return "intimate"
    if d < 1.2: return "personal"
    if d < 3.6: return "social"
    return "public"

MAX_SPEED = {"public": 1.2, "social": 0.6,
             "personal": 0.2, "intimate": 0.0}

for distance in [5.0, 3.0, 1.5, 0.8, 0.3]:
    z = zone(distance)
    print(f"person at {distance:3.1f} m: zone {z:8s} "
          f"-> max speed {MAX_SPEED[z]:.1f} m/s")
