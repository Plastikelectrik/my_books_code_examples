# Runs on the Raspberry Pi. Save as rover.py
import threading
import time
import serial

class Rover:
    def __init__(self, port="/dev/ttyACM0",
                 baud=115200):
        self.link = serial.Serial(port, baud,
                                  timeout=0.1)
        time.sleep(2)              # Arduino reset
        self.ticks = (0, 0)
        self.distance_cm = -1.0
        self.last_status = 0.0
        self._lock = threading.Lock()
        self._run = True
        self._t = threading.Thread(target=self._reader,
                                   daemon=True)
        self._t.start()

    def _reader(self):
        while self._run:
            raw = self.link.readline()
            line = raw.decode("ascii", "ignore").strip()
            if not line.startswith("S,"):
                continue
            try:
                _, l, r, d = line.split(",")
                with self._lock:
                    self.ticks = (int(l), int(r))
                    self.distance_cm = float(d)
                    self.last_status = time.monotonic()
            except ValueError:
                pass               # ignore bad lines

    def velocity(self, left_m_s, right_m_s):
        msg = f"V,{left_m_s:.3f},{right_m_s:.3f}\n"
        self.link.write(msg.encode("ascii"))

    def pwm(self, left, right):
        msg = f"M,{int(left)},{int(right)}\n"
        self.link.write(msg.encode("ascii"))

    def stop(self):
        self.velocity(0, 0)

    def status(self):
        with self._lock:
            age = time.monotonic() - self.last_status
            return self.ticks, self.distance_cm, age

    def close(self):
        self.stop()
        self._run = False
        self._t.join(timeout=1)
        self.link.close()
