MAZE = ["#########",
        "#S..#...#",
        "#.#.#.#.#",
        "#.#...#.#",
        "#.#####.#",
        "#...#...#",
        "###.#.#.#",
        "#.....#G#",
        "#########"]
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # N E S W

def find(ch):
    for r, row in enumerate(MAZE):
        if ch in row:
            return r, row.index(ch)

def free(r, c):
    return MAZE[r][c] != "#"

def wall_follow(left=True, limit=200):
    """Left-hand (or right-hand) rule."""
    (r, c), goal = find("S"), find("G")
    d, path = 1, [(r, c)]             # start facing east
    turns = [-1, 0, 1, 2] if left else [1, 0, -1, 2]
    for _ in range(limit):
        if (r, c) == goal:
            return path
        for t in turns:              # prefer one side
            nd = (d + t) % 4
            dr, dc = DIRS[nd]
            if free(r + dr, c + dc):
                d = nd
                r, c = r + dr, c + dc
                path.append((r, c))
                break
    return None

def simplify(path):
    """Remove dead ends: cut loops back to a cell."""
    out = []
    for p in path:
        if p in out:
            out = out[:out.index(p) + 1]
        else:
            out.append(p)
    return out

for left in (True, False):
    p = wall_follow(left)
    s = simplify(p)
    name = "left-hand " if left else "right-hand"
    print(f"{name}: explored {len(p) - 1} steps, "
          f"shortcut {len(s) - 1} steps")
best = simplify(wall_follow(True))
grid = [list(row) for row in MAZE]
for r, c in best[1:-1]:
    grid[r][c] = "*"
print("\n".join("".join(row) for row in grid))
