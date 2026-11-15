# Apply temperature to scores and sample many times
import numpy as np
from collections import Counter

words = ["robot", "box", "door", "banana"]
scores = np.array([3.0, 2.0, 1.0, -1.0])   # model scores
rng = np.random.default_rng(0)

for temp in [0.2, 1.0, 2.0]:
    p = np.exp(scores / temp)
    p = p / p.sum()                 # softmax
    picks = rng.choice(words, size=1000, p=p)
    c = Counter(picks)
    share = ", ".join(f"{w} {c[w] / 10:.0f}%"
                      for w in words)
    print(f"T={temp}: {share}")
