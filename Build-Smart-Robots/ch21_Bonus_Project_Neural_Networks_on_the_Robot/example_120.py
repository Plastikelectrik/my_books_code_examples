import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

rng = np.random.default_rng(0)
d = load_digits()
X = d.data / 16.0                       # scale to 0..1
Y = np.eye(10)[d.target]                # one-hot labels
Xtr, Xte, Ytr, Yte = train_test_split(
    X, Y, test_size=0.25, random_state=0)

H = 32                                  # hidden size
W1 = rng.normal(0, np.sqrt(2 / 64), (64, H))
b1 = np.zeros(H)
W2 = rng.normal(0, np.sqrt(2 / H), (H, 10))
b2 = np.zeros(10)

def forward(X):
    z1 = X @ W1 + b1
    h = np.maximum(0, z1)               # ReLU
    z2 = h @ W2 + b2
    z2 -= z2.max(axis=1, keepdims=True)  # stability
    p = np.exp(z2)
    p /= p.sum(axis=1, keepdims=True)   # softmax
    return z1, h, p

def accuracy(X, Y):
    return (forward(X)[2].argmax(1) == Y.argmax(1)).mean()

lr, batch = 0.1, 32
for epoch in range(30):
    order = rng.permutation(len(Xtr))
    for i in range(0, len(Xtr), batch):
        idx = order[i:i + batch]
        x, yb = Xtr[idx], Ytr[idx]
        z1, h, p = forward(x)
        # backpropagation (cross-entropy + softmax)
        dz2 = (p - yb) / len(x)
        dW2 = h.T @ dz2
        db2 = dz2.sum(0)
        dh = dz2 @ W2.T
        dz1 = dh * (z1 > 0)               # ReLU slope
        dW1 = x.T @ dz1
        db1 = dz1.sum(0)
        W1 -= lr * dW1
        b1 -= lr * db1
        W2 -= lr * dW2
        b2 -= lr * db2
    if epoch % 10 == 9:
        print(f"epoch {epoch + 1:2d}: train "
              f"{accuracy(Xtr, Ytr):.3f}  test "
              f"{accuracy(Xte, Yte):.3f}")
np.savez("digits_net.npz", W1=W1, b1=b1, W2=W2, b2=b2)
