# Create a 6x8 RGB image as a NumPy array
import numpy as np

img = np.zeros((6, 8, 3), dtype=np.uint8)  # black
img[:, :] = (200, 200, 200)                # gray floor
img[1:4, 2:5] = (220, 30, 30)              # red box
img[4:6, 6:8] = (30, 30, 220)              # blue box
print("shape (rows, cols, channels):", img.shape)
print("pixel at row 2, col 3:", img[2, 3])
print("pixel at row 5, col 7:", img[5, 7])
print("total numbers:", img.size)
