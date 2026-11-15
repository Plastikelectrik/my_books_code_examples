# Forward pass, backpropagation and gradient descent
import numpy as np

rng = np.random.default_rng(0)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], float)
y = np.array([[0], [1], [1], [0]], float)

W1 = rng.normal(0, 1, (2, 4))    # input -> 4 hidden
b1 = np.zeros((1, 4))
W2 = rng.normal(0, 1, (4, 1))    # hidden -> output
b2 = np.zeros((1, 1))
sig = lambda z: 1 / (1 + np.exp(-z))
lr = 1.0

for epoch in range(1, 5001):
    h = sig(X @ W1 + b1)              # forward
    out = sig(h @ W2 + b2)
    loss = np.mean((out - y) ** 2)
    d_out = (out - y) * out * (1 - out)      # backward
    d_h = (d_out @ W2.T) * h * (1 - h)
    W2 -= lr * h.T @ d_out                   # update
    b2 -= lr * d_out.sum(axis=0, keepdims=True)
    W1 -= lr * X.T @ d_h
    b1 -= lr * d_h.sum(axis=0, keepdims=True)
    if epoch in (1, 500, 2000, 5000):
        print(f"epoch {epoch:4d}: loss {loss:.4f}")

print("predictions:", out.round(2).ravel())
