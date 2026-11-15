# Attractive goal force plus repulsive obstacle force
import math

goal = (5.0, 0.0)
obstacle = (2.5, 0.2)
x, y = 0.0, 0.0
for step in range(1, 61):
    fx, fy = goal[0] - x, goal[1] - y          # attract
    dx, dy = x - obstacle[0], y - obstacle[1]
    d = math.hypot(dx, dy)
    if d < 1.0:                                # repel
        k = 0.8 * (1 / d - 1.0) / d**2
        fx += k * dx
        fy += k * dy
    norm = math.hypot(fx, fy)
    x += 0.1 * fx / norm                 # step 0.1 m
    y += 0.1 * fy / norm
    if step % 10 == 0:
        d_obs = math.dist((x, y), obstacle)
        print(f"step {step}: ({x:5.2f}, {y:5.2f}) "
              f"obstacle {d_obs:.2f} m away")
    if math.dist((x, y), goal) < 0.1:
        print(f"goal reached at step {step}")
        break
