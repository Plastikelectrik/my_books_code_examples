import math

PATH = [(0.0, 0.0), (1.0, 0.0), (1.0, 1.0),
        (2.0, 1.0)]

def lookahead_point(x, y, path, L):
    """First point on the path at distance >= L,
    searching from the end of the closest segment."""
    for (x1, y1), (x2, y2) in zip(path, path[1:]):
        for k in range(21):
            t = k / 20
            px = x1 + (x2 - x1) * t
            py = y1 + (y2 - y1) * t
            if math.hypot(px - x, py - y) >= L and \
                    (px - x) * (x2 - x1) + \
                    (py - y) * (y2 - y1) > 0:
                return px, py
    return path[-1]

x, y, th = 0.0, -0.1, 0.0       # start slightly off
v, L, dt = 0.2, 0.3, 0.05
max_err, t = 0.0, 0.0
while math.dist((x, y), PATH[-1]) > 0.05 and t < 30:
    px, py = lookahead_point(x, y, PATH, L)
    alpha = math.atan2(py - y, px - x) - th
    alpha = math.atan2(math.sin(alpha), math.cos(alpha))
    w = 2 * v * math.sin(alpha) / L
    x += v * math.cos(th) * dt
    y += v * math.sin(th) * dt
    th += w * dt
    t += dt
print(f"reached the end in {t:.1f} s "
      f"at ({x:.2f}, {y:.2f})")
