import heapq
import math
import numpy as np

def astar(grid, start, goal):
    rows, cols = grid.shape
    moves = [(-1, 0, 1), (1, 0, 1), (0, -1, 1),
             (0, 1, 1), (-1, -1, 1.414),
             (-1, 1, 1.414), (1, -1, 1.414),
             (1, 1, 1.414)]
    def h(n):
        return math.hypot(n[0] - goal[0],
                          n[1] - goal[1])
    open_heap = [(h(start), 0.0, start)]
    came_from = {start: None}
    g = {start: 0.0}
    expanded = 0
    while open_heap:
        f, cost, cur = heapq.heappop(open_heap)
        if cost > g[cur]:
            continue                 # outdated entry
        expanded += 1
        if cur == goal:
            path = []
            while cur is not None:
                path.append(cur)
                cur = came_from[cur]
            return path[::-1], expanded
        for dr, dc, step in moves:
            nr, nc = cur[0] + dr, cur[1] + dc
            if not (0 <= nr < rows and 0 <= nc < cols):
                continue
            if grid[nr, nc]:
                continue
            new = cost + step
            if new < g.get((nr, nc), float("inf")):
                g[(nr, nc)] = new
                came_from[(nr, nc)] = cur
                heapq.heappush(open_heap,
                               (new + h((nr, nc)), new,
                                (nr, nc)))
    return None, expanded

if __name__ == "__main__":
    grid = np.load("room.npy")
    path, n = astar(grid, (10, 5), (50, 74))
    length = sum(math.dist(a, b) for a, b in
                 zip(path, path[1:])) * 0.05
    print(f"path: {len(path)} cells, "
          f"{length:.2f} m, expanded {n} cells")
