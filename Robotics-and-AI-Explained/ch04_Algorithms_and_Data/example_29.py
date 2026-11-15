# Min-max scaling and standardization with NumPy
import numpy as np

weight_g = np.array([400, 1200, 5100, 8500])
length_m = np.array([0.15, 0.30, 0.45, 0.60])

def min_max(x):
    return (x - x.min()) / (x.max() - x.min())

def standardize(x):
    return (x - x.mean()) / x.std()

np.set_printoptions(precision=2, suppress=True)
print("weight min-max :", min_max(weight_g))
print("length min-max :", min_max(length_m))
print("weight standard:", standardize(weight_g))
