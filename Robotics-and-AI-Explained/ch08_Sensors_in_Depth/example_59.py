# Compare a biased sensor and a noisy sensor
import numpy as np

rng = np.random.default_rng(0)
true_value = 100.0                     # cm
biased = true_value + 4 + rng.normal(0, 0.3, 50)
noisy = true_value + rng.normal(0, 3.0, 50)

for name, data in [("biased", biased), ("noisy", noisy)]:
    error = data.mean() - true_value
    print(f"{name:6s}: mean error {error:+.2f} cm, "
          f"spread {data.std():.2f} cm")

calibrated = biased - 4.0              # remove known bias
print(f"after calibration: mean error "
      f"{calibrated.mean() - true_value:+.2f} cm")
