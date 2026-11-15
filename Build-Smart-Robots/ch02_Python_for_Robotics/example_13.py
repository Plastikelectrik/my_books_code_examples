import math
import matplotlib.pyplot as plt

x, y, th = 0.0, 0.0, 0.0
xs, ys = [x], [y]
dt = 0.1
for _ in range(130):
    v, w = 0.3, 0.5          # m/s, rad/s
    x += v * math.cos(th) * dt
    y += v * math.sin(th) * dt
    th += w * dt
    xs.append(x)
    ys.append(y)

plt.plot(xs, ys, "b-", label="path")
plt.plot(xs[0], ys[0], "go", label="start")
plt.axis("equal")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.legend()
plt.savefig("circle_path.png", dpi=120)
print("radius should be v/w =", 0.3 / 0.5, "m")
