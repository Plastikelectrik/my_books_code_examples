# Runs on a Raspberry Pi with a camera module
from picamera2 import Picamera2
import cv2

cam = Picamera2()
cfg = cam.create_preview_configuration(
    main={"size": (320, 240), "format": "RGB888"})
cam.configure(cfg)
cam.start()
frame = cam.capture_array()   # NumPy array
print("frame shape:", frame.shape)
cv2.imwrite("pi_frame.png", frame)
cam.stop()
