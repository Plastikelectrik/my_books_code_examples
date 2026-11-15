import math
import numpy as np

RES, W, H = 0.05, 4.0, 3.0
rows, cols = int(H / RES), int(W / RES)

# --- the true world (unknown to the robot) ---
truth = np.zeros((rows, cols), bool)
truth[0, :] = truth[-1, :] = True
truth[:, 0] = truth[:, -1] = True
truth[20:40, 30:34] = True            # a cabinet

def cast(x, y, ang, max_r=3.5):
    for r in np.arange(0, max_r, RES / 2):
        c = int((x + r * math.cos(ang)) / RES)
        rw = int((y + r * math.sin(ang)) / RES)
        if not (0 <= rw < rows and 0 <= c < cols):
            return max_r
        if truth[rw, c]:
            return r
    return max_r

logodds = np.zeros((rows, cols))
L_FREE, L_OCC = -0.4, 0.85
poses = [(0.5, 0.5), (1.0, 2.5), (3.5, 2.5), (3.5, 0.5)]
for (px, py) in poses:
    for k in range(180):                # 2-degree steps
        a = math.radians(2 * k)
        r = cast(px, py, a)
        for s in np.arange(0, r - RES, RES / 2):
            c = int((px + s * math.cos(a)) / RES)
            rw = int((py + s * math.sin(a)) / RES)
            logodds[rw, c] += L_FREE
        if r < 3.5:
            c = int((px + r * math.cos(a)) / RES)
            rw = int((py + r * math.sin(a)) / RES)
            logodds[rw, c] += L_OCC

occ = logodds > 0.5
free = logodds < -0.5
known = occ | free
print(f"known cells: {100 * known.mean():.0f} %")
agree = (occ == truth)[known].mean()
print(f"agreement with truth (known cells): "
      f"{100 * agree:.1f} %")
np.save("built_map.npy", occ.astype(np.uint8))
