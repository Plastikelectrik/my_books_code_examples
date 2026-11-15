import numpy as np

rng = np.random.default_rng(2)
DOORS = [2.0, 3.0, 7.5]          # door positions (m)
LENGTH, N = 10.0, 1000

def at_door(x):
    return min(abs(x - d) for d in DOORS) < 0.3

true_x = 1.2                     # unknown to the robot
particles = rng.uniform(0, LENGTH, N)

for step in range(14):
    move = 0.5
    true_x += move + rng.normal(0, 0.02)
    # 1. predict
    particles += move + rng.normal(0, 0.05, N)
    # 2. weight: sensor sees a door? (90 % reliable)
    z = at_door(true_x)
    if rng.random() < 0.1:
        z = not z                 # sensor mistake
    match = np.array([at_door(p) == z
                      for p in particles])
    w = np.where(match, 0.9, 0.1)
    w[particles > LENGTH] = 0     # left the corridor
    w /= w.sum()
    # 3. resample
    idx = rng.choice(N, N, p=w)
    particles = particles[idx]
    est, spread = particles.mean(), particles.std()
    if step % 3 and step != 13:
        continue
    print(f"step {step:2d}: true {true_x:5.2f}  "
          f"estimate {est:5.2f} +/- {spread:4.2f}  "
          f"door={'yes' if z else 'no '}")
