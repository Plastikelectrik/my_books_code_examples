import numpy as np
import cv2

aruco = cv2.aruco
d = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
SIZE_M = 0.10                  # printed marker: 10 cm
K = np.array([[600, 0, 320],   # camera matrix
              [0, 600, 240],
              [0, 0, 1]], dtype=np.float64)
dist = np.zeros(5)             # assume no distortion

# Create a view of a marker 0.8 m ahead, 0.1 m right
true_t = np.array([0.10, 0.0, 0.80])
h = SIZE_M / 2
obj = np.array([[-h, h, 0], [h, h, 0], [h, -h, 0],
                [-h, -h, 0]], dtype=np.float64)
# marker faces the camera: rotated 180 deg about x
facing = np.array([np.pi, 0.0, 0.0])
img_pts, _ = cv2.projectPoints(obj, facing,
                               true_t, K, dist)
marker = aruco.generateImageMarker(d, 3, 200)
src = np.float32([[0, 0], [199, 0], [199, 199],
                  [0, 199]])
H = cv2.getPerspectiveTransform(
    src, img_pts.reshape(4, 2).astype(np.float32))
scene = cv2.warpPerspective(marker, H, (640, 480),
                            borderValue=255)

det = aruco.ArucoDetector(d, aruco.DetectorParameters())
corners, ids, _ = det.detectMarkers(scene)
ok, rvec, tvec = cv2.solvePnP(
    obj, corners[0][0].astype(np.float64), K, dist,
    flags=cv2.SOLVEPNP_IPPE_SQUARE)
x, y, z = tvec.flatten()
angle = np.degrees(np.arctan2(x, z))
print(f"marker ID {ids.flatten()[0]}")
print(f"distance ahead: {z:.2f} m, sideways: {x:.2f} m")
print(f"bearing: {angle:+.1f} degrees")
