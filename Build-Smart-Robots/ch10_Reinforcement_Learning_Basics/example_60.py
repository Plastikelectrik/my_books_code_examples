import numpy as np

GRID = ["S...#.",
        ".##.#.",
        "...H..",
        ".#.##.",
        ".#....",
        "...#.C"]
ROWS, COLS = len(GRID), len(GRID[0])
ACTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
NAMES = "^v<>"

def step(r, c, a):
    dr, dc = ACTIONS[a]
    nr, nc = r + dr, c + dc
    if not (0 <= nr < ROWS and 0 <= nc < COLS) \
            or GRID[nr][nc] == "#":
        return r, c, -5, False      # bumped a wall
    cell = GRID[nr][nc]
    if cell == "H":
        return nr, nc, -50, True    # fell down
    if cell == "C":
        return nr, nc, 50, True     # charged!
    return nr, nc, -1, False

rng = np.random.default_rng(0)
Q = np.zeros((ROWS, COLS, 4))
alpha, gamma = 0.1, 0.95
episodes = 2000
for ep in range(episodes):
    eps = max(0.05, 1.0 - ep / 1000)
    r, c, done, steps = 0, 0, False, 0
    while not done and steps < 100:
        if rng.random() < eps:
            a = int(rng.integers(4))
        else:
            a = int(np.argmax(Q[r, c]))
        nr, nc, rew, done = step(r, c, a)
        target = rew
        if not done:
            target += gamma * Q[nr, nc].max()
        Q[r, c, a] += alpha * (target - Q[r, c, a])
        r, c, steps = nr, nc, steps + 1

# Show the learned policy
for i in range(ROWS):
    row = ""
    for j in range(COLS):
        cell = GRID[i][j]
        if cell in "#HC":
            row += cell
        else:
            row += NAMES[int(np.argmax(Q[i, j]))]
    print(row)

# Follow the learned policy from the start
r, c, n = 0, 0, 0
done = False
while not done and n < 30:
    r, c, _, done = step(r, c, int(np.argmax(Q[r, c])))
    n += 1
print("steps to the charger:", n)
print("ends on:", GRID[r][c])
