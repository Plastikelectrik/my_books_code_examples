import numpy as np
import cv2

# --- test image: light floor with a curved dark line ---
img = np.full((240, 320, 3), 200, np.uint8)
pts = np.array([[205, 239], [215, 180], [240, 120],
                [280, 60]], np.int32)
cv2.polylines(img, [pts], False, (30, 30, 30), 18)

def line_error(frame):
    h, w = frame.shape[:2]
    roi = frame[int(h * 0.75):, :]        # bottom 25 %
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(
        gray, 0, 255,
        cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    m = cv2.moments(mask)
    if m["m00"] == 0:
        return None                       # line lost
    cx = m["m10"] / m["m00"]              # centroid x
    return (cx - w / 2) / (w / 2)         # -1..+1

err = line_error(img)
print(f"line error: {err:+.2f}")
if err > 0.05:
    print("line is right of center: turn right")
elif err < -0.05:
    print("line is left of center: turn left")
else:
    print("line is centered: go straight")
