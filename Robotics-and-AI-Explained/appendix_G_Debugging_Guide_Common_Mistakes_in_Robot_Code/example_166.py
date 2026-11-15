import numpy as np

pixels = np.array([200, 250], dtype=np.uint8)
print("uint8 sum :", pixels + 10)
print("safe sum  :", pixels.astype(np.int32) + 10)
safe = pixels.astype(int) + 10
print("clipped   :", np.clip(safe, 0, 255))
