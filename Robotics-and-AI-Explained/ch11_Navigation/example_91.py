# Shortest path with BFS, counting explored cells
from collections import deque

grid = ["..........",
        "...####...",
        "......#...",
        ".####.#...",
        "......#..."]
start, goal = (4, 0), (0, 9)
R, C = len(grid), len(grid[0])

def bfs():
    came = {start: None}
    queue = deque([start])
    while queue:
        cur = queue.popleft()
        if cur == goal:
            break
        r, c = cur
        for nr, nc in ((r+1, c), (r-1, c),
                       (r, c+1), (r, c-1)):
            if (0 <= nr < R and 0 <= nc < C
                    and grid[nr][nc] == "."
                    and (nr, nc) not in came):
                came[(nr, nc)] = cur
                queue.append((nr, nc))
    path, node = [], goal
    while node is not None:
        path.append(node)
        node = came[node]
    return path[::-1], len(came)

path, explored = bfs()
print("path length:", len(path) - 1, "steps")
print("cells explored:", explored)
