import math
import random
import statistics

random.seed(1)                       # repeatable results
samples = [random.gauss(50, 2) for _ in range(5)]
print("samples:", [round(s, 1) for s in samples])
print(f"mean  : {statistics.mean(samples):.2f}")
print(f"median: {statistics.median(samples):.2f}")
print(f"sqrt 2: {math.sqrt(2):.4f}")
print(f"pi    : {math.pi:.4f}")
