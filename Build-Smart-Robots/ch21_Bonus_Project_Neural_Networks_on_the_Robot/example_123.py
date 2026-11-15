import numpy as np
import cv2

def to_digit_input(crop_bgr):
    """Dark digit on white card -> 64 values, 0..1."""
    g = cv2.cvtColor(crop_bgr, cv2.COLOR_BGR2GRAY)
    g = 255 - g                        # digit bright
    g = cv2.resize(g, (8, 8),
                   interpolation=cv2.INTER_AREA)
    return (g.astype(float) / 255.0).reshape(1, 64)

# test with a synthetic card showing "1"
card = np.full((120, 120, 3), 255, np.uint8)
cv2.line(card, (60, 20), (60, 100), (0, 0, 0), 14)
x = to_digit_input(card)
print("input shape:", x.shape)
print("brightest column:",
      int(x.reshape(8, 8).sum(0).argmax()))
