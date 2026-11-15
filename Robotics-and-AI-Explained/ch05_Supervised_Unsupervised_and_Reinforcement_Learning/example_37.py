# Fit polynomials of different degrees to noisy data
import numpy as np

rng = np.random.default_rng(1)
x = np.linspace(0, 1, 30)
y = np.sin(2 * np.pi * x) + rng.normal(0, 0.2, 30)
train = np.arange(30) % 3 != 0   # 20 train, 10 test
test = ~train

for degree in [1, 3, 9, 15]:
    coeffs = np.polyfit(x[train], y[train], degree)
    err_tr = np.mean((np.polyval(coeffs, x[train])
                      - y[train]) ** 2)
    err_te = np.mean((np.polyval(coeffs, x[test])
                      - y[test]) ** 2)
    print(f"degree {degree:2d}: train error {err_tr:.3f},"
          f" test error {err_te:.3f}")
