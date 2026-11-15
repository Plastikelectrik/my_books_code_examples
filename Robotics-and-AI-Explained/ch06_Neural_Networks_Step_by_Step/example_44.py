# The same learning rule cannot solve XOR
data = [((0, 0), 0), ((0, 1), 1),
        ((1, 0), 1), ((1, 1), 0)]
w1 = w2 = b = 0.0
for epoch in range(100):
    for (x1, x2), target in data:
        out = 1 if w1 * x1 + w2 * x2 + b > 0 else 0
        err = target - out
        w1 += 0.1 * err * x1
        w2 += 0.1 * err * x2
        b += 0.1 * err
correct = sum((1 if w1*x1 + w2*x2 + b > 0 else 0) == t
              for (x1, x2), t in data)
print(f"correct after 100 epochs: {correct} of 4")
