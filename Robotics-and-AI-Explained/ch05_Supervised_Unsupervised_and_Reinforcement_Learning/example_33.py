# Train and test a classifier on synthetic package data
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

rng = np.random.default_rng(0)
n = 200
small = np.column_stack([rng.normal(1.5, 0.6, n),
                         rng.normal(25, 6, n)])
large = np.column_stack([rng.normal(6.0, 1.5, n),
                         rng.normal(55, 10, n)])
X = np.vstack([small, large])
y = np.array([0] * n + [1] * n)   # 0 small, 1 large

X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.25, random_state=1)
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_tr, y_tr)
acc = model.score(X_te, y_te)
print(f"test accuracy: {acc:.3f}")
print("prediction for (3.5 kg, 40 cm):",
      model.predict([[3.5, 40]])[0])
