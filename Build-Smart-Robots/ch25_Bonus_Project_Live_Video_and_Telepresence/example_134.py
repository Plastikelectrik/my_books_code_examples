import os
import numpy as np
import cv2

W, H, FPS = 320, 240, 15
fourcc = cv2.VideoWriter_fourcc(*"MJPG")
out = cv2.VideoWriter("drive.avi", fourcc, FPS, (W, H))
for i in range(45):                     # 3 seconds
    f = np.full((H, W, 3), 30, np.uint8)
    cv2.rectangle(f, (10 + i * 6, 100),
                  (40 + i * 6, 140), (0, 200, 0), -1)
    cv2.putText(f, f"t={i / FPS:.1f}s  v=0.15 m/s",
                (8, 230), cv2.FONT_HERSHEY_SIMPLEX,
                0.45, (255, 255, 255), 1)
    out.write(f)
out.release()
cap = cv2.VideoCapture("drive.avi")
n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("frames in file:", n)
print("file size:", os.path.getsize("drive.avi") // 1024,
      "KB")
