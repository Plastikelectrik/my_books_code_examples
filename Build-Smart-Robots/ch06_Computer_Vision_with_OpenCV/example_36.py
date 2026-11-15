import numpy as np
import cv2

rng = np.random.default_rng(0)
# --- make a test image (gray floor, noise, ball) ---
img = np.full((240, 320, 3), 110, np.uint8)
noise = rng.integers(0, 25, img.shape, dtype=np.uint8)
img = cv2.add(img, noise)
cv2.circle(img, (220, 140), 30, (0, 140, 255), -1)

# --- detect ---
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
low = np.array([10, 120, 80])     # H, S, V
high = np.array([25, 255, 255])
mask = cv2.inRange(hsv, low, high)

contours, _ = cv2.findContours(
    mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
if contours:
    big = max(contours, key=cv2.contourArea)
    (x, y), r = cv2.minEnclosingCircle(big)
    print(f"ball at x={x:.0f}, y={y:.0f}, "
          f"radius={r:.0f} px")
    cv2.circle(img, (int(x), int(y)), int(r),
               (255, 0, 0), 2)
cv2.imwrite("ball_found.png", img)
cv2.imwrite("ball_mask.png", mask)
