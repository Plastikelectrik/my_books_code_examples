# Shortest path with A*; draw the path on the grid
import heapq
import matplotlib.pyplot as plt

grid = ["..........",
        "...####...",
        "......#...",
        ".####.#...",
        "......#..."]
start, goal = (4, 0), (0, 9)
R, C = len(grid), len(grid[0])
h = lambda p: abs(p[0] - goal[0]) + abs(p[1] - goal[1])

open_set = [(h(start), 0, start)]
came, g = {start: None}, {start: 0}
explored = 0
while open_set:
    f, cost, cur = heapq.heappop(open_set)
    explored += 1
    if cur == goal:
        break
    r, c = cur
    for nb in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
        nr, nc = nb
        if not (0 <= nr < R and 0 <= nc < C):
            continue
        if grid[nr][nc] == "#":
            continue
        new_cost = cost + 1
        if new_cost < g.get(nb, 1e9):
            g[nb], came[nb] = new_cost, cur
            item = (new_cost + h(nb), new_cost, nb)
            heapq.heappush(open_set, item)

path, node = [], goal
while node:
    path.append(node)
    node = came[node]
path.reverse()
print("path length:", len(path) - 1, "steps")
print("cells expanded:", explored)

img = [[1 if ch == "#" else 0 for ch in row]
       for row in grid]
plt.figure(figsize=(5, 2.6))
plt.imshow(img, cmap="Greys")
plt.plot([p[1] for p in path], [p[0] for p in path],
         "o-", color="tab:orange")
plt.title("A* path from bottom-left to top-right")
plt.xticks([]); plt.yticks([])
plt.tight_layout()
plt.savefig("astar.png")
