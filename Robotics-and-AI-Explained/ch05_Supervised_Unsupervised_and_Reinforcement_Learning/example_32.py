# Classify packages by comparing with known examples
import math
from collections import Counter

# (weight kg, length cm) -> label
train = [((1.0, 20), "small"), ((1.5, 25), "small"),
         ((0.5, 15), "small"), ((2.0, 30), "small"),
         ((7.0, 60), "large"), ((8.5, 70), "large"),
         ((6.0, 55), "large"), ((9.0, 65), "large")]

def distance(a, b):
    # weight is scaled by 10 so both features matter
    return math.hypot((a[0] - b[0]) * 10, a[1] - b[1])

def knn(sample, k=3):
    near = sorted(
        train, key=lambda t: distance(sample, t[0]))[:k]
    votes = Counter(label for _, label in near)
    return votes.most_common(1)[0][0]

for pkg in [(1.2, 22), (7.5, 58), (4.0, 40)]:
    print(pkg, "->", knn(pkg))
