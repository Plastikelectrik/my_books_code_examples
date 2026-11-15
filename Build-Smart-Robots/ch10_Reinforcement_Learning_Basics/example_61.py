import numpy as np

rng = np.random.default_rng(1)
N_STATES, N_ACTIONS = 7, 5
TURNS = [-0.30, -0.12, 0.0, 0.12, 0.30]

def to_state(offset):
    """Map offset (-1..1) to a zone 0..6."""
    edges = [-0.6, -0.3, -0.1, 0.1, 0.3, 0.6]
    return int(np.digitize(offset, edges))

def reward(offset):
    if abs(offset) > 1.0:
        return -10.0
    return 1.0 - 2.0 * abs(offset)

def run_episode(Q, eps, learn=True, steps=300):
    offset, drift, total = 0.0, 0.0, 0.0
    for _ in range(steps):
        s = to_state(offset)
        if rng.random() < eps:
            a = int(rng.integers(N_ACTIONS))
        else:
            a = int(np.argmax(Q[s]))
        drift = 0.9 * drift + rng.normal(0, 0.02)
        offset += drift - TURNS[a] * 0.5
        r = reward(offset)
        total += r
        lost = abs(offset) > 1.0
        if learn:
            s2 = to_state(offset)
            target = r if lost else \
                r + 0.9 * Q[s2].max()
            Q[s, a] += 0.1 * (target - Q[s, a])
        if lost:
            break
    return total

Q = np.zeros((N_STATES, N_ACTIONS))
before = np.mean([run_episode(Q, 1.0, False)
                  for _ in range(50)])
for ep in range(3000):
    run_episode(Q, max(0.05, 1 - ep / 1500))
after = np.mean([run_episode(Q, 0.0, False)
                 for _ in range(50)])
print(f"average reward, random policy: {before:7.1f}")
print(f"average reward, learned:       {after:7.1f}")
names = ["hard L", "left", "straight", "right",
         "hard R"]
zones = ["far L", "left", "sl. L", "center",
         "sl. R", "right", "far R"]
for z in range(N_STATES):
    print(f"line {zones[z]:6s} -> "
          f"{names[int(np.argmax(Q[z]))]}")
