import numpy as np
import cv2

# Create a 120 x 160 black image with 3 color channels
img = np.zeros((120, 160, 3), dtype=np.uint8)

# OpenCV uses BGR order: (blue, green, red)
cv2.rectangle(img, (20, 30), (60, 90), (0, 0, 255), -1)
cv2.circle(img, (115, 60), 25, (0, 255, 0), -1)

print("shape (rows, cols, channels):", img.shape)
print("pixel at row 60, col 40 (BGR):", img[60, 40])
print("pixel at row 60, col 115 (BGR):", img[60, 115])
cv2.imwrite("shapes.png", img)
