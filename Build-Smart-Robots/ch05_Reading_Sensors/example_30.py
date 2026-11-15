import numpy as np
from collections import deque

rng = np.random.default_rng(42)
n = 200
truth = np.where(np.arange(n) < 100, 50.0, 30.0)
data = truth + rng.normal(0, 1.5, n)
bad = rng.random(n) < 0.05
data[bad] = rng.uniform(5, 400, bad.sum())

def moving_avg(xs, k=5):
    win, out = deque(maxlen=k), []
    for x in xs:
        win.append(x)
        out.append(sum(win) / len(win))
    return np.array(out)

def median(xs, k=5):
    win, out = deque(maxlen=k), []
    for x in xs:
        win.append(x)
        out.append(float(np.median(win)))
    return np.array(out)

def ema(xs, alpha=0.3):
    y, out = xs[0], []
    for x in xs:
        y += alpha * (x - y)
        out.append(y)
    return np.array(out)

results = {
    "raw": data,
    "moving average": moving_avg(data),
    "median": median(data),
    "exponential": ema(data),
    "median + exp.": ema(median(data)),
}
for name, y in results.items():
    err = np.abs(y - truth)[5:]
    print(f"{name:15s} mean error {err.mean():6.2f} cm"
          f"   worst {err.max():6.1f} cm")
