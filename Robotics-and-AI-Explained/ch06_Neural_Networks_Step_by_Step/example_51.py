# Slide a 3x3 filter over a small image
import numpy as np

img = np.zeros((6, 6))
img[:, 3:] = 9                 # dark right half
kernel = np.array([[-1, 0, 1],
                   [-1, 0, 1],
                   [-1, 0, 1]])  # vertical edges

out = np.zeros((4, 4))
for r in range(4):
    for c in range(4):
        patch = img[r:r + 3, c:c + 3]
        out[r, c] = np.sum(patch * kernel)
print("image:")
print(img.astype(int))
print("edge map:")
print(out.astype(int))
