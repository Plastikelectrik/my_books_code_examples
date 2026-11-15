import math

words = ["blue", "clear", "grey", "beautiful", "green"]
scores = [4.0, 2.5, 2.0, 1.5, -1.0]

def softmax(xs, temperature):
    exps = [math.exp(x / temperature) for x in xs]
    total = sum(exps)
    return [e / total for e in exps]

temps = (0.2, 0.7, 1.5)
table = [softmax(scores, t) for t in temps]
head = "".join(f"  T={t:<4}" for t in temps)
print("word      " + head)
for i, w in enumerate(words):
    cells = "".join(f"{col[i]:8.1%}" for col in table)
    print(f"{w:10s}{cells}")
