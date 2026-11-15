import time
import numpy as np
import cv2

def fake_camera(n=30, w=320, h=240):
    """Generate moving test frames (no camera needed)."""
    for i in range(n):
        f = np.full((h, w, 3), 40, np.uint8)
        x = int(20 + i * (w - 40) / n)
        cv2.circle(f, (x, h // 2), 18, (0, 165, 255), -1)
        cv2.putText(f, f"frame {i}", (8, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255), 1)
        yield f

def mjpeg_parts(frames, quality=70):
    """Yield multipart chunks for an MJPEG stream."""
    params = [cv2.IMWRITE_JPEG_QUALITY, quality]
    for f in frames:
        ok, jpg = cv2.imencode(".jpg", f, params)
        if not ok:
            continue
        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n"
               + jpg.tobytes() + b"\r\n")

for q in (90, 70, 40):
    t0 = time.perf_counter()
    sizes = [len(p) for p in mjpeg_parts(fake_camera(),
                                         quality=q)]
    dt = (time.perf_counter() - t0) / len(sizes)
    kb = sum(sizes) / len(sizes) / 1024
    mbit = kb * 15 * 8 / 1024           # at 15 fps
    print(f"q={q}: {kb:4.1f} KB/frame, {mbit:4.2f} "
          f"Mbit/s, encode {dt * 1000:3.1f} ms")
