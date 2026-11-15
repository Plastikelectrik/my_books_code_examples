# Compare sigmoid, tanh and ReLU at a few points
import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def relu(z):
    return np.maximum(0, z)

z = np.array([-3.0, -1.0, 0.0, 1.0, 3.0])
np.set_printoptions(precision=3, suppress=True)
print("z      :", z)
print("sigmoid:", sigmoid(z))
print("tanh   :", np.tanh(z))
print("relu   :", relu(z))
