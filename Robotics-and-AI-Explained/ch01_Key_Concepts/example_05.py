# Average many noisy readings to estimate the truth
import random

random.seed(2)
true_distance = 50.0

def read_sensor():
    return true_distance + random.gauss(0, 2.0)

for n in [1, 5, 20, 100]:
    readings = [read_sensor() for _ in range(n)]
    average = sum(readings) / n
    error = abs(average - true_distance)
    print(f"{n:3d} readings: avg {average:6.2f}"
          f" cm, error {error:.2f} cm")
