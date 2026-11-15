import numpy as np

rng = np.random.default_rng(7)
FS = 100                         # samples per second

def drive(surface, seconds=60):
    n = FS * seconds
    t = np.arange(n) / FS
    if surface == "floor":
        z = 0.03 * np.sin(2 * np.pi * 18 * t) \
            + rng.normal(0, 0.02, n)
    elif surface == "carpet":
        z = 0.015 * np.sin(2 * np.pi * 9 * t) \
            + rng.normal(0, 0.015, n)
    else:   # gravel: random shocks
        z = rng.normal(0, 0.06, n)
        shocks = rng.random(n) < 0.03
        z[shocks] += rng.normal(0, 0.4, shocks.sum())
    return z

data = {s: drive(s) for s in ["floor", "carpet",
                              "gravel"]}
for s, z in data.items():
    print(f"{s:7s} samples={len(z)}  "
          f"std={z.std():.3f} g")
np.savez("terrain.npz", **data)
