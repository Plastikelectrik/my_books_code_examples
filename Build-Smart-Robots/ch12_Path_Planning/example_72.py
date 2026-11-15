import numpy as np
from astar import astar

def line_free(grid, a, b):
    n = int(max(abs(b[0] - a[0]), abs(b[1] - a[1]))) + 1
    rs = np.linspace(a[0], b[0], n).round().astype(int)
    cs = np.linspace(a[1], b[1], n).round().astype(int)
    return not grid[rs, cs].any()

def smooth(grid, path):
    out, i = [path[0]], 0
    while i < len(path) - 1:
        j = len(path) - 1
        while j > i + 1 and not line_free(grid, path[i],
                                          path[j]):
            j -= 1
        out.append(path[j])
        i = j
    return out

grid = np.load("inflated.npy")
path, _ = astar(grid, (10, 5), (50, 74))
short = smooth(grid, path)
print("points before:", len(path),
      "after:", len(short))
for p in short:
    print("  waypoint (row, col):", p)
