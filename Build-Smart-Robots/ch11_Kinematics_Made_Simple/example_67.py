import math

def go_to_goal(x, y, th, gx, gy,
               v_max=0.25, k_w=2.0):
    dx, dy = gx - x, gy - y
    dist = math.hypot(dx, dy)
    target = math.atan2(dy, dx)
    err = math.atan2(math.sin(target - th),
                     math.cos(target - th))
    # slow down when far off course or close to goal
    v = min(v_max, 0.8 * dist) * max(0.0, math.cos(err))
    w = k_w * err
    return v, w, dist

x, y, th = 0.0, 0.0, 0.0
goal = (1.0, 0.8)
dt, t = 0.05, 0.0
while True:
    v, w, dist = go_to_goal(x, y, th, *goal)
    if dist < 0.02:
        break
    x += v * math.cos(th) * dt
    y += v * math.sin(th) * dt
    th += w * dt
    t += dt
print(f"reached ({x:.3f}, {y:.3f}) in {t:.1f} s")
