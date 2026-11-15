import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix

rng = np.random.default_rng(7)
n_good, n_bad = 1900, 100
good = np.column_stack([rng.normal(50.0, 0.4, n_good),
                        rng.normal(180, 12, n_good),
                        rng.poisson(1.0, n_good)])
bad = np.column_stack([rng.normal(50.6, 0.9, n_bad),
                       rng.normal(160, 20, n_bad),
                       rng.poisson(4.0, n_bad)])
X = np.vstack([good, bad])
y = np.array([0] * n_good + [1] * n_bad)   # 1 = defect

X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.4, stratify=y, random_state=0)
model = RandomForestClassifier(n_estimators=200,
                               random_state=0)
model.fit(X_tr, y_tr)
prob = model.predict_proba(X_te)[:, 1]

print("thr  found  missed  false alarms  cost")
for thr in [0.5, 0.3, 0.15]:
    pred = (prob >= thr).astype(int)
    tn, fp, fn, tp = confusion_matrix(y_te, pred).ravel()
    cost = fn * 200 + fp * 5   # misses cost more
    print(f"{thr:4.2f} {tp:6d} {fn:7d} {fp:13d}"
          f" {cost:5d}")
names = ["size", "brightness", "spots"]
for name, imp in zip(names, model.feature_importances_):
    print(f"importance {name:10s}: {imp:.2f}")
