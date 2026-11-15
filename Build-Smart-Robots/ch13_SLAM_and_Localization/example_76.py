import math
import numpy as np

rng = np.random.default_rng(0)
MARKERS = {0: (0.0, 1.5), 1: (4.0, 0.5),
           2: (2.0, 3.0)}
N = 2000

def wrap(a):
    return (a + np.pi) % (2 * np.pi) - np.pi

def observe(pose):
    """Range and bearing to all markers (with noise)."""
    x, y, th = pose
    out = {}
    for mid, (mx, my) in MARKERS.items():
        r = math.hypot(mx - x, my - y)
        b = wrap(math.atan2(my - y, mx - x) - th)
        out[mid] = (r + rng.normal(0, 0.05),
                    b + rng.normal(0, 0.03))
    return out

true = np.array([0.5, 0.5, 0.3])
P = np.column_stack([rng.uniform(0, 4, N),
                     rng.uniform(0, 3, N),
                     rng.uniform(-np.pi, np.pi, N)])
v, w, dt = 0.2, 0.15, 0.5
for step in range(15):
    # move the true robot and the particles
    true[0] += v * dt * math.cos(true[2])
    true[1] += v * dt * math.sin(true[2])
    true[2] += w * dt
    P[:, 0] += (v * dt + rng.normal(0, 0.02, N)) \
        * np.cos(P[:, 2])
    P[:, 1] += (v * dt + rng.normal(0, 0.02, N)) \
        * np.sin(P[:, 2])
    P[:, 2] += w * dt + rng.normal(0, 0.02, N)
    # weight with all observed markers
    logw = np.zeros(N)
    for mid, (r, b) in observe(true).items():
        mx, my = MARKERS[mid]
        pr = np.hypot(mx - P[:, 0], my - P[:, 1])
        pb = wrap(np.arctan2(my - P[:, 1],
                             mx - P[:, 0]) - P[:, 2])
        logw += -0.5 * ((pr - r) / 0.1) ** 2
        logw += -0.5 * (wrap(pb - b) / 0.1) ** 2
    wts = np.exp(logw - logw.max())
    wts /= wts.sum()
    P = P[rng.choice(N, N, p=wts)]
    est = P[:, :2].mean(axis=0)
    err = math.dist(est, true[:2])
    if step % 3 == 0 or step == 14:
        print(f"step {step:2d}: position error "
              f"{100 * err:5.1f} cm")
