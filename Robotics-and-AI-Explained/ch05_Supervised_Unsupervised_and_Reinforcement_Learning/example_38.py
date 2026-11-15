# Cluster robot stop locations into three groups
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

rng = np.random.default_rng(2)
centers = [(2, 2), (8, 3), (5, 8)]
stops = np.vstack([rng.normal(c, 0.8, size=(40, 2))
                   for c in centers])

km = KMeans(n_clusters=3, n_init=10, random_state=0)
labels = km.fit_predict(stops)
for c in sorted(km.cluster_centers_.round(1).tolist()):
    print("station at", c)

plt.figure(figsize=(5, 3.2))
plt.scatter(stops[:, 0], stops[:, 1], c=labels, s=10)
plt.scatter(*km.cluster_centers_.T, marker="X", s=150,
            c="black")
plt.title("Robot stops and charging stations")
plt.gca().set_aspect("equal")
plt.tight_layout()
plt.savefig("kmeans.png")
