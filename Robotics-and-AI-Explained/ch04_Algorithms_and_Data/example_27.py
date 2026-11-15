# Basic statistics of temperature readings
import numpy as np

temps = np.array([21.2, 21.5, 21.3, 21.8, 35.0,
                  21.4, 21.6, 21.1, 21.7, 21.3])
print("mean   :", round(temps.mean(), 2))
print("median :", round(float(np.median(temps)), 2))
print("std    :", round(temps.std(), 2))
print("min/max:", temps.min(), temps.max())
