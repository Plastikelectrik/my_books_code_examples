# Drive a figure-eight and save a plot of the path
import math
import matplotlib.pyplot as plt

WB, dt = 0.30, 0.05
x = y = th = 0.0
xs, ys = [x], [y]
N = 126               # steps for one full circle
for i in range(2 * N):
    turn = 0.15 if i < N else -0.15
    vl, vr = 0.4 - turn, 0.4 + turn
    v, w = (vr + vl) / 2, (vr - vl) / WB
    x += v * math.cos(th) * dt
    y += v * math.sin(th) * dt
    th += w * dt
    xs.append(x)
    ys.append(y)

plt.figure(figsize=(5, 3))
plt.plot(xs, ys)
plt.gca().set_aspect("equal")
plt.title("Differential drive: figure-eight")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.tight_layout()
plt.savefig("figure_eight.png")
print(f"end point: ({x:.2f}, {y:.2f})")
