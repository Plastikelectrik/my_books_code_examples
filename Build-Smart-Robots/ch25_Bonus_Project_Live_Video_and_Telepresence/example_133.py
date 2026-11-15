# Runs on the Raspberry Pi with a camera
# (pip install flask)
import time
import cv2
from flask import Flask, Response

app = Flask(__name__)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

def frames(fps=12):
    period = 1.0 / fps
    while True:
        t0 = time.monotonic()
        ok, f = cap.read()
        if not ok:
            break
        cv2.putText(f, time.strftime("%H:%M:%S"), (8, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255), 1)
        ok, jpg = cv2.imencode(".jpg", f,
                               [cv2.IMWRITE_JPEG_QUALITY,
                                70])
        yield (b"--frame\r\nContent-Type: image/jpeg"
               b"\r\n\r\n" + jpg.tobytes() + b"\r\n")
        time.sleep(max(0.0, period - (time.monotonic()
                                       - t0)))

@app.get("/video")
def video():
    return Response(frames(), mimetype=
                    "multipart/x-mixed-replace; "
                    "boundary=frame")

@app.get("/")
def page():
    return ('<h2>Rover camera</h2>'
            '<img src="/video" width="640">')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, threaded=True)
