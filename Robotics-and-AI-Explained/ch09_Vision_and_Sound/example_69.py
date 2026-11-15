# Weighted sum of the three color channels
import numpy as np

img = np.full((4, 6, 3), 200, dtype=np.uint8)
img[1:3, 1:3] = (220, 30, 30)        # red square
img[1:3, 4:6] = (30, 200, 30)        # green square
weights = np.array([0.299, 0.587, 0.114])
gray = (img @ weights).round().astype(np.uint8)
print(gray)
