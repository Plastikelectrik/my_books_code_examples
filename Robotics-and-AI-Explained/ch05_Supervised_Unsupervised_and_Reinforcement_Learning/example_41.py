# Learn a path in a 4x5 grid with obstacles
import random

random.seed(1)
grid = ["S..#.",
        ".#...",
        "...#.",
        "#...C"]
H, W = len(grid), len(grid[0])
moves = {"U": (-1, 0), "D": (1, 0),
         "L": (0, -1), "R": (0, 1)}
Q = {(r, c): {a: 0.0 for a in moves}
     for r in range(H) for c in range(W)}

def step(state, a):
    r, c = state[0] + moves[a][0], state[1] + moves[a][1]
    inside = 0 <= r < H and 0 <= c < W
    if not inside or grid[r][c] == "#":
        return state, -5, False        # bump: penalty
    if grid[r][c] == "C":
        return (r, c), 20, True        # charger found
    return (r, c), -1, False           # each step costs

alpha, gamma, eps = 0.5, 0.9, 0.2
for episode in range(400):
    s = (0, 0)
    for _ in range(50):
        if random.random() < eps:
            a = random.choice(list(moves))
        else:
            a = max(Q[s], key=Q[s].get)
        s2, rew, done = step(s, a)
        best_next = max(Q[s2].values())
        Q[s][a] += alpha * (rew + gamma * best_next
                            - Q[s][a])
        s = s2
        if done:
            break

s, path = (0, 0), []
for _ in range(20):
    a = max(Q[s], key=Q[s].get)
    path.append(a)
    s, _, done = step(s, a)
    if done:
        break
print("learned path:", " ".join(path))
print("steps:", len(path))
