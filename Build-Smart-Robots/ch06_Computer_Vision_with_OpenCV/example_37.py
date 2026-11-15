import numpy as np
import cv2

rng = np.random.default_rng(1)
mask = np.zeros((100, 100), np.uint8)
cv2.circle(mask, (50, 50), 25, 255, -1)
# add salt-and-pepper noise
specks = rng.random(mask.shape)
mask[specks < 0.03] = 255      # white specks
mask[specks > 0.97] = 0        # black holes

k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
clean = cv2.morphologyEx(mask, cv2.MORPH_OPEN, k)
clean = cv2.morphologyEx(clean, cv2.MORPH_CLOSE, k)

def blobs(m):
    n, _ = cv2.connectedComponents(m)
    return n - 1     # minus the background

print("regions before:", blobs(mask))
print("regions after: ", blobs(clean))
