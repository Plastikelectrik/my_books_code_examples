import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

rng = np.random.default_rng(0)
X = rng.normal(10, 3, (200, 2))
X_tr, X_te = train_test_split(X, random_state=0)

scaler = StandardScaler().fit(X_tr)  # train only
X_tr_s = scaler.transform(X_tr)
X_te_s = scaler.transform(X_te)      # same scaler
print("train mean:", X_tr_s.mean(axis=0).round(2))
print("test mean :", X_te_s.mean(axis=0).round(2))
