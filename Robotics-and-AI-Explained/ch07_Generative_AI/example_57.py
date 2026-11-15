# Learn the shape of data, then sample new points
import numpy as np
from sklearn.mixture import GaussianMixture

rng = np.random.default_rng(1)
real = np.vstack([rng.normal((2, 2), 0.5, (100, 2)),
                  rng.normal((7, 5), 0.8, (100, 2))])
gm = GaussianMixture(n_components=2, random_state=0)
gm.fit(real)
new, _ = gm.sample(6)
print("learned centers:")
print(gm.means_.round(2))
print("new synthetic points:")
print(new.round(2))
