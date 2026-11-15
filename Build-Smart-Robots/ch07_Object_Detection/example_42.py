import cv2

aruco = cv2.aruco
dictionary = aruco.getPredefinedDictionary(
    aruco.DICT_4X4_50)       # 50 different IDs

for marker_id in [0, 1, 2]:
    img = aruco.generateImageMarker(dictionary,
                                    marker_id, 400)
    # white border helps detection
    img = cv2.copyMakeBorder(img, 40, 40, 40, 40,
                             cv2.BORDER_CONSTANT,
                             value=255)
    cv2.imwrite(f"marker_{marker_id}.png", img)
print("saved marker_0.png, marker_1.png, marker_2.png")
