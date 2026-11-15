import numpy as np
import cv2

# Four reference points: pixel (u, v) -> table (x, y) m
px = np.float32([[102, 380], [538, 372],
                 [530, 88], [110, 95]])
table = np.float32([[0.08, 0.12], [0.08, -0.12],
                    [0.24, -0.12], [0.24, 0.12]])
H, _ = cv2.findHomography(px, table)

def pixel_to_table(u, v):
    p = H @ np.array([u, v, 1.0])
    return p[0] / p[2], p[1] / p[2]

for u, v in [(320, 234), (110, 95), (420, 300)]:
    x, y = pixel_to_table(u, v)
    print(f"pixel ({u},{v}) -> table "
          f"x={x:.3f} m, y={y:+.3f} m")
