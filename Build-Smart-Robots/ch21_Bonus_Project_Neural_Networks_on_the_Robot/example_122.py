import time
import numpy as np
from sklearn.datasets import load_digits

w = np.load("digits_net.npz")
X = load_digits().data / 16.0

def predict(x):
    h = np.maximum(0, x @ w["W1"] + w["b1"])
    return (h @ w["W2"] + w["b2"]).argmax(-1)

one = X[:1]
t0 = time.perf_counter()
for _ in range(1000):
    predict(one)
single = (time.perf_counter() - t0) / 1000
t0 = time.perf_counter()
predict(X)
batch = (time.perf_counter() - t0) / len(X)
print(f"one image at a time: {single * 1e6:6.1f} us")
print(f"in a batch:          {batch * 1e6:6.2f} us/image")
