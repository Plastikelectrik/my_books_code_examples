import numpy as np

H, W = 60, 80
rng = np.random.default_rng(7)

def frame(person_x=None):
    """A noisy gray garden with an optional person."""
    img = np.full((H, W), 90.0) + rng.normal(0, 3, (H, W))
    if person_x is not None:
        img[20:50, person_x:person_x + 8] = 200
    return img

def motion(prev, cur, thresh=25, min_pixels=60):
    diff = np.abs(cur - prev) > thresh
    count = int(diff.sum())
    if count < min_pixels:
        return None
    ys, xs = np.nonzero(diff)
    box = (int(xs.min()), int(ys.min()),
           int(xs.max()), int(ys.max()))
    return count, box

prev = frame()
for t, x in enumerate([None, None, 10, 20, 30, None]):
    cur = frame(x)
    m = motion(prev, cur)
    if m:
        print(f"t={t}: motion, {m[0]} pixels, box {m[1]}")
    else:
        print(f"t={t}: quiet")
    prev = cur
