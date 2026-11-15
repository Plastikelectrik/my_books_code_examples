# Gradient magnitude shows the outline of a square
import numpy as np

img = np.zeros((9, 9))
img[2:7, 2:7] = 100                     # bright square
kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
ky = kx.T

edges = np.zeros((7, 7))
for r in range(7):
    for c in range(7):
        patch = img[r:r + 3, c:c + 3]
        gx = np.sum(patch * kx)
        gy = np.sum(patch * ky)
        edges[r, c] = np.hypot(gx, gy)
print((edges / edges.max() * 9).round().astype(int))
