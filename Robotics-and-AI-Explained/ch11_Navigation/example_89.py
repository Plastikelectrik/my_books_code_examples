# Compare true and estimated position on a square path
import math, random

random.seed(4)
true = [0.0, 0.0, 0.0]          # x, y, heading
est = [0.0, 0.0, 0.0]

def move(pose, dist, turn):
    pose[2] += turn
    pose[0] += dist * math.cos(pose[2])
    pose[1] += dist * math.sin(pose[2])

for lap in range(1, 4):
    for side in range(4):
        for _ in range(10):                 # 10 x 0.1 m
            move(true, 0.1, 0)
            move(est, 0.1 * random.gauss(1, 0.02),
                 random.gauss(0, 0.01))
        move(true, 0, math.pi / 2)          # turn left
        move(est, 0, math.pi / 2 + random.gauss(0, 0.02))
    err = math.dist(true[:2], est[:2])
    print(f"after lap {lap}: error {err:.3f} m")
