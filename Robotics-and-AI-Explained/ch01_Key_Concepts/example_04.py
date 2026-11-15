# Real sensors add random errors (noise)
import random

random.seed(1)  # same random numbers every run
true_distance = 50.0

for i in range(5):
    noise = random.gauss(0, 2.0)  # mean 0, std 2 cm
    reading = true_distance + noise
    print(f"reading {i + 1}: {reading:.2f} cm")
