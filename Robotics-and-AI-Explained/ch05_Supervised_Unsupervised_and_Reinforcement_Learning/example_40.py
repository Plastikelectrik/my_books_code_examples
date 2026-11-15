# Epsilon-greedy learning of the best station
import random

random.seed(0)
true_speed = [0.6, 0.9, 0.75]     # unknown to the robot
estimate = [0.0, 0.0, 0.0]
count = [0, 0, 0]
epsilon = 0.1             # explore 10% of the time

for visit in range(500):
    if random.random() < epsilon:
        s = random.randrange(3)               # explore
    else:
        s = estimate.index(max(estimate))     # exploit
    reward = random.gauss(true_speed[s], 0.2)
    count[s] += 1
    estimate[s] += (reward - estimate[s]) / count[s]

print("visits   :", count)
print("estimates:", [round(e, 2) for e in estimate])
