# Runs on the Raspberry Pi with a camera and rover.py
import time
import numpy as np
import cv2

aruco = cv2.aruco
DICT = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
DET = aruco.ArucoDetector(DICT,
                          aruco.DetectorParameters())
SIZE = 0.08                     # printed marker (m)
K = np.array([[600, 0, 320], [0, 600, 240],
              [0, 0, 1]], float)  # use calibration!
h = SIZE / 2
OBJ = np.array([[-h, h, 0], [h, h, 0], [h, -h, 0],
                [-h, -h, 0]], float)

def marker_offset(frame, marker_id):
    corners, ids, _ = DET.detectMarkers(frame)
    if ids is None:
        return None
    for c, i in zip(corners, ids.flatten()):
        if i == marker_id:
            ok, rv, tv = cv2.solvePnP(
                OBJ, c[0].astype(float), K, np.zeros(5),
                flags=cv2.SOLVEPNP_IPPE_SQUARE)
            x, _, z = tv.flatten()
            return z, np.arctan2(x, z)  # dist, bearing
    return None

def dock(bot, cap, marker_id, stop_at=0.15):
    lost = 0
    while True:
        ok, frame = cap.read()
        m = marker_offset(frame, marker_id) if ok \
            else None
        if m is None:
            lost += 1
            bot.stop()
            if lost > 20:
                return False    # marker not found
            time.sleep(0.05)
            continue
        lost = 0
        dist, bearing = m
        if dist <= stop_at:
            bot.stop()
            return True
        v = min(0.08, 0.5 * (dist - stop_at))
        w = -1.5 * bearing      # turn toward marker
        bot.velocity(v - w * 0.077, v + w * 0.077)
        time.sleep(0.05)
