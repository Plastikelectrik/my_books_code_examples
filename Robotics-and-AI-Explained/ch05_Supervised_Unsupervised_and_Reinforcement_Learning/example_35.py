# Predict battery use (%) from trip distance (m)
import numpy as np
from sklearn.linear_model import LinearRegression

rng = np.random.default_rng(5)
distance = rng.uniform(50, 800, 40)
noise = rng.normal(0, 1.2, 40)
battery_used = 2 + 0.025 * distance + noise

model = LinearRegression()
model.fit(distance.reshape(-1, 1), battery_used)
a = model.coef_[0]
b = model.intercept_
print(f"learned: used = {b:.2f} + {a:.4f} * distance")
for d in [100, 400, 1000]:
    pred = model.predict([[d]])[0]
    print(f"{d:4d} m -> {pred:5.1f} % battery")
