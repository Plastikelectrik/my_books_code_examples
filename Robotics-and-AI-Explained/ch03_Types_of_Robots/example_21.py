# Each robot moves 10% toward the center of the group
import random

random.seed(7)
robots = [[random.uniform(0, 10), random.uniform(0, 10)]
          for _ in range(8)]

def spread(rs):
    cx = sum(r[0] for r in rs) / len(rs)
    cy = sum(r[1] for r in rs) / len(rs)
    return max(((r[0]-cx)**2 + (r[1]-cy)**2) ** 0.5
               for r in rs)

for step in range(0, 31):
    if step % 10 == 0:
        d = spread(robots)
        print(f"step {step:2d}: spread {d:.2f} m")
    cx = sum(r[0] for r in robots) / len(robots)
    cy = sum(r[1] for r in robots) / len(robots)
    for r in robots:
        r[0] += 0.1 * (cx - r[0])
        r[1] += 0.1 * (cy - r[1])
