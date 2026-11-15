from collections import deque

GRID = ["#########",
        "#.......#",
        "#####.###",
        "#########"]
FREE = {(r, c) for r, row in enumerate(GRID)
        for c, ch in enumerate(row) if ch == "."}
MOVES = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]

def plan(start, goal, reserved, max_t=40):
    """Space-time BFS: avoid cells reserved at time t."""
    q = deque([(start, 0)])
    came = {(start, 0): None}
    while q:
        cell, t = q.popleft()
        if cell == goal and all(
                (goal, k) not in reserved
                for k in range(t, max_t)):
            path, node = [], (cell, t)
            while node:
                path.append(node[0])
                node = came[node]
            return path[::-1]
        if t >= max_t:
            continue
        for dr, dc in MOVES:          # (0, 0) = wait
            nxt = (cell[0] + dr, cell[1] + dc)
            if nxt not in FREE or (nxt, t + 1) in came:
                continue
            if (nxt, t + 1) in reserved:
                continue              # occupied then
            # no swapping places head-on
            if (("edge", nxt, cell, t)) in reserved:
                continue
            came[(nxt, t + 1)] = (cell, t)
            q.append((nxt, t + 1))
    return None

def reserve(path, reserved, horizon=40):
    for t, cell in enumerate(path):
        reserved.add((cell, t))
        if t > 0:
            prev = path[t - 1]
            reserved.add(("edge", prev, cell, t - 1))
    for t in range(len(path), horizon):
        reserved.add((path[-1], t))   # stays at goal

robots = {"A": ((1, 1), (1, 7)), "B": ((1, 7), (1, 1))}
reserved, paths = set(), {}
for name, (s, g) in robots.items():  # A has priority
    p = plan(s, g, reserved)
    if p is None:
        print(f"robot {name}: no plan found!")
        continue
    paths[name] = p
    reserve(p, reserved)
    print(f"robot {name}: {len(p) - 1} steps")
T = max(len(p) for p in paths.values())
for t in range(T):
    row = list(GRID[1])
    bay = list(GRID[2])
    for name, p in paths.items():
        r, c = p[min(t, len(p) - 1)]
        (row if r == 1 else bay)[c] = name
    print(f"t={t:2d} {''.join(row)}  {''.join(bay)}")
