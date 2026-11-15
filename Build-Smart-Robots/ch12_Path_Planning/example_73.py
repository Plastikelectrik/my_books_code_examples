import math
import random

random.seed(4)
OBST = [(1.5, 1.0, 0.5), (2.6, 2.0, 0.45),
        (3.2, 0.8, 0.35)]           # (x, y, radius)
START, GOAL = (0.3, 0.3), (3.7, 2.7)
STEP, W, H = 0.15, 4.0, 3.0

def free(p):
    return all(math.dist(p, (ox, oy)) > r + 0.1
               for ox, oy, r in OBST)

def segment_free(a, b):
    n = max(2, int(math.dist(a, b) / 0.02))
    return all(free((a[0] + (b[0] - a[0]) * t / n,
                     a[1] + (b[1] - a[1]) * t / n))
               for t in range(n + 1))

nodes, parent = [START], {START: None}
for it in range(5000):
    rnd = GOAL if random.random() < 0.1 else \
        (random.uniform(0, W), random.uniform(0, H))
    near = min(nodes, key=lambda n: math.dist(n, rnd))
    d = math.dist(near, rnd)
    if d == 0:
        continue
    new = (near[0] + STEP * (rnd[0] - near[0]) / d,
           near[1] + STEP * (rnd[1] - near[1]) / d)
    if not segment_free(near, new):
        continue
    nodes.append(new)
    parent[new] = near
    if math.dist(new, GOAL) < STEP and \
            segment_free(new, GOAL):
        parent[GOAL] = new
        break

path, n = [], GOAL
while n is not None:
    path.append(n)
    n = parent[n]
path.reverse()
length = sum(math.dist(a, b) for a, b in
             zip(path, path[1:]))
print(f"iterations: {it + 1}, tree nodes: {len(nodes)}")
print(f"path: {len(path)} points, {length:.2f} m")
print(f"straight-line distance: "
      f"{math.dist(START, GOAL):.2f} m")
