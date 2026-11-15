import numpy as np

# 8 distance readings in meters (0.0 = no echo)
scan = np.array([1.2, 0.0, 0.8, 3.5, 0.0, 0.4, 2.2, 9.9])

valid = scan[(scan > 0.05) & (scan < 8.0)]
print("valid readings:", valid)
print("closest obstacle:", valid.min(), "m")
print("average distance:", round(valid.mean(), 2), "m")

# Angles of the 8 beams (evenly spread over 360 deg)
angles = np.linspace(0, 2 * np.pi, 8, endpoint=False)
x = scan * np.cos(angles)
y = scan * np.sin(angles)
print("x:", np.round(x, 2))
