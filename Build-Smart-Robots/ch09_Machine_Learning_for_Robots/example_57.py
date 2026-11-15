import numpy as np
from sklearn.ensemble import IsolationForest

rng = np.random.default_rng(0)

def motor_window(health=1.0):
    """Features: [mean current A, current std,
    speed at PWM 150 (m/s)]"""
    cur = rng.normal(0.35 / health, 0.02)
    std = rng.normal(0.03 / health, 0.004)
    spd = rng.normal(0.62 * health, 0.02)
    return [cur, std, spd]

normal = np.array([motor_window() for _ in range(500)])
model = IsolationForest(contamination=0.01,
                        random_state=0).fit(normal)

tests = {"healthy": 1.0, "slightly worn": 0.9,
         "failing": 0.7}
for name, h in tests.items():
    X = np.array([motor_window(h) for _ in range(200)])
    flagged = (model.predict(X) == -1).mean()
    print(f"{name:14s} flagged as anomaly: "
          f"{100 * flagged:5.1f} %")
