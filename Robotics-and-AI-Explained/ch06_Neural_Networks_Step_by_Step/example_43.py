# Learn weights from examples with the perceptron rule
data = [((0, 0), 0), ((0, 1), 0),
        ((1, 0), 0), ((1, 1), 1)]
w1 = w2 = b = 0.0
lr = 0.1

for epoch in range(1, 21):
    errors = 0
    for (x1, x2), target in data:
        out = 1 if w1 * x1 + w2 * x2 + b > 0 else 0
        err = target - out
        if err != 0:
            errors += 1
            w1 += lr * err * x1
            w2 += lr * err * x2
            b += lr * err
    if errors == 0:
        print(f"learned in epoch {epoch}")
        break
print(f"w1={w1:.1f}, w2={w2:.1f}, b={b:.1f}")
