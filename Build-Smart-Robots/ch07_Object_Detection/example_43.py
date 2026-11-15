import numpy as np
import cv2

aruco = cv2.aruco
d = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
marker = aruco.generateImageMarker(d, 7, 200)

# --- build a 480 x 640 scene, marker in perspective ---
scene = np.full((480, 640), 180, np.uint8)
src = np.float32([[0, 0], [199, 0], [199, 199],
                  [0, 199]])
dst = np.float32([[300, 150], [440, 170], [430, 300],
                  [290, 290]])
H = cv2.getPerspectiveTransform(src, dst)
warp = cv2.warpPerspective(marker, H, (640, 480),
                           borderValue=255)
mask = cv2.warpPerspective(
    np.full_like(marker, 255), H, (640, 480))
scene[mask > 0] = warp[mask > 0]
# white paper around the marker
cv2.rectangle(scene, (270, 130), (460, 320), 255, 3)

# --- detect ---
detector = aruco.ArucoDetector(
    d, aruco.DetectorParameters())
corners, ids, _ = detector.detectMarkers(scene)
print("found IDs:", ids.flatten().tolist())
c = corners[0][0]
center = c.mean(axis=0)
print("center (x, y):", np.round(center, 1))
cv2.imwrite("scene.png", scene)
