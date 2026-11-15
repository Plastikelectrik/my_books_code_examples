# Convert a simulated 2D lidar scan to x, y points
import math
import matplotlib.pyplot as plt

def wall_distance(angle_deg):
    # robot in a 4 m x 3 m room at (1.5, 1.0)
    a = math.radians(angle_deg)
    dx, dy = math.cos(a), math.sin(a)
    hits = []
    if dx > 1e-9: hits.append((4 - 1.5) / dx)
    if dx < -1e-9: hits.append(-1.5 / dx)
    if dy > 1e-9: hits.append((3 - 1.0) / dy)
    if dy < -1e-9: hits.append(-1.0 / dy)
    return min(hits)

angles = range(0, 360, 5)
scan = [wall_distance(a) for a in angles]
xs = [d * math.cos(math.radians(a))
      for a, d in zip(angles, scan)]
ys = [d * math.sin(math.radians(a))
      for a, d in zip(angles, scan)]
print("readings:", len(scan))
print("closest wall:", round(min(scan), 2), "m")

plt.figure(figsize=(5, 3.4))
plt.scatter(xs, ys, s=8)
plt.scatter([0], [0], marker="^", s=80)
plt.gca().set_aspect("equal")
plt.title("Lidar scan seen from the robot")
plt.tight_layout()
plt.savefig("lidar_scan.png")
