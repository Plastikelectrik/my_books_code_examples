# Probability of each next word after "the"
from collections import Counter

text = ("the robot moves . the robot stops . "
        "the box falls . the robot lifts the box . "
        "the door opens .")
words = text.split()
pairs = Counter(zip(words, words[1:]))
after_the = {b: n for (a, b), n in pairs.items()
             if a == "the"}
total = sum(after_the.values())
for word, n in sorted(after_the.items(),
                      key=lambda kv: -kv[1]):
    print(f"P({word:5s} | the) = {n}/{total} "
          f"= {n / total:.2f}")
