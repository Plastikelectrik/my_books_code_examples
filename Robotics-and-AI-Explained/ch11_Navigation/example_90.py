# 1D Monte Carlo localization with a door detector
import random

random.seed(2)
doors = [1.0, 2.5, 6.0]          # door positions (m)
LENGTH = 10.0

def sees_door(x):
    return any(abs(x - d) < 0.3 for d in doors)

true_x = 0.2
N = 500
particles = [random.uniform(0, LENGTH) for _ in range(N)]

for step in range(1, 13):
    true_x += 0.6                                # move
    particles = [p + 0.6 + random.gauss(0, 0.05)
                 for p in particles]
    z = sees_door(true_x)                        # sense
    weights = []
    for p in particles:
        if not 0 <= p <= LENGTH:
            weights.append(0.0)       # outside corridor
        elif sees_door(p) == z:
            weights.append(0.95)
        else:
            weights.append(0.05)
    particles = random.choices(particles, weights, k=N)
    mean = sum(particles) / N
    spread = (sum((p - mean) ** 2 for p in particles)
              / N) ** 0.5
    seen = "door" if z else "wall"
    print(f"step {step:2d}: true {true_x:4.1f} m, est "
          f"{mean:4.1f} m, spread {spread:4.2f} ({seen})")
