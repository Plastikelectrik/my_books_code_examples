# Needs a camera. Press q in the window to quit.
import cv2

cap = cv2.VideoCapture(0)            # first camera
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
if not cap.isOpened():
    raise SystemExit("No camera found")

while True:
    ok, frame = cap.read()
    if not ok:
        break
    cv2.imshow("Rover camera", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
