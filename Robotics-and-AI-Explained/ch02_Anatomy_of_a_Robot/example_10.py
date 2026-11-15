# Plot all points the two-link arm can reach
import math
import matplotlib.pyplot as plt

L1, L2 = 0.30, 0.20
xs, ys = [], []
for a1 in range(0, 181, 3):        # shoulder 0..180
    for a2 in range(-150, 151, 3):  # elbow -150..150
        t1, t2 = math.radians(a1), math.radians(a2)
        xs.append(L1*math.cos(t1) + L2*math.cos(t1+t2))
        ys.append(L1*math.sin(t1) + L2*math.sin(t1+t2))

plt.figure(figsize=(5, 3))
plt.scatter(xs, ys, s=1)
plt.gca().set_aspect("equal")
plt.title("Workspace of a two-link arm")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.tight_layout()
plt.savefig("workspace.png", dpi=150)
print("points:", len(xs))
print("max reach:", round(max(
    math.hypot(x, y) for x, y in zip(xs, ys)), 3), "m")
