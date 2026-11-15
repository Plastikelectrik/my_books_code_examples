# Runs on Rover: camera + Arduino on USB
import time
import numpy as np
import cv2
import serial

link = serial.Serial("/dev/ttyACM0", 115200)
time.sleep(2)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
LOW, HIGH = (10, 120, 80), (25, 255, 255)
K = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,
                              (5, 5))

def send(left, right):
    link.write(f"M,{left},{right}\n".encode())

try:
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, np.array(LOW),
                           np.array(HIGH))
        mask = cv2.morphologyEx(mask,
                                cv2.MORPH_OPEN, K)
        cs, _ = cv2.findContours(
            mask, cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
        if not cs:
            send(60, -60)        # search: spin
            continue
        big = max(cs, key=cv2.contourArea)
        (x, y), r = cv2.minEnclosingCircle(big)
        err = (x - 160) / 160
        base = 140 if r < 45 else 0
        turn = 120 * err
        send(int(base + turn), int(base - turn))
finally:
    send(0, 0)
    cap.release()
