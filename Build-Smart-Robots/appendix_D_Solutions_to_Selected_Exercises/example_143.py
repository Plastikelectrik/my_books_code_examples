import math

def wrap(a):
    return math.atan2(math.sin(a), math.cos(a))

WAYPOINTS = [(1, 0), (1, 1), (0, 1), (0, 0)]
FINAL_HEADING = math.radians(0)
x, y, th, dt, t = 0.0, 0.0, 0.0, 0.05, 0.0
i = 0
while i < len(WAYPOINTS):
    gx, gy = WAYPOINTS[i]
    dist = math.hypot(gx - x, gy - y)
    if dist < 0.05:
        i += 1
        continue
    err = wrap(math.atan2(gy - y, gx - x) - th)
    v = min(0.25, 0.8 * dist) * max(0.0, math.cos(err))
    w = 2.0 * err
    x += v * math.cos(th) * dt
    y += v * math.sin(th) * dt
    th += w * dt
    t += dt
while abs(wrap(FINAL_HEADING - th)) > math.radians(2):
    th += 2.0 * wrap(FINAL_HEADING - th) * dt
    t += dt
print(f"done in {t:.1f} s at ({x:.2f}, {y:.2f}), "
      f"heading {math.degrees(wrap(th)):.1f} deg")
