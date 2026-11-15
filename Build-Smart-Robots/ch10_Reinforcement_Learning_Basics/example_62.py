# Runs on the Raspberry Pi with rover.py and a camera
import numpy as np
import cv2
from rover import Rover

Q = np.load("line_q.npy")
TURNS = [-0.30, -0.12, 0.0, 0.12, 0.30]
EDGES = [-0.6, -0.3, -0.1, 0.1, 0.3, 0.6]

def line_offset(frame):
    h, w = frame.shape[:2]
    roi = cv2.cvtColor(frame[int(h * 0.75):],
                       cv2.COLOR_BGR2GRAY)
    _, m = cv2.threshold(roi, 0, 255,
                         cv2.THRESH_BINARY_INV
                         + cv2.THRESH_OTSU)
    mom = cv2.moments(m)
    if mom["m00"] == 0:
        return None
    return (mom["m10"] / mom["m00"] - w / 2) / (w / 2)

bot, cap = Rover(), cv2.VideoCapture(0)
try:
    while True:
        ok, frame = cap.read()
        off = line_offset(frame) if ok else None
        if off is None:
            bot.stop()
            continue
        s = int(np.digitize(off, EDGES))
        turn = TURNS[int(np.argmax(Q[s]))]
        v = 0.12                       # m/s
        bot.velocity(v + turn * 0.3, v - turn * 0.3)
finally:
    bot.close()
