import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score

f = np.load("features.npz")
X, y = f["X"], f["y"]

models = {
    "k-NN (k=5)": make_pipeline(
        StandardScaler(), KNeighborsClassifier(5)),
    "random forest": RandomForestClassifier(
        n_estimators=200, random_state=0),
}
for name, model in models.items():
    scores = cross_val_score(model, X, y, cv=5)
    print(f"{name:14s} accuracy {scores.mean():.3f}"
          f" (+/- {scores.std():.3f})")
