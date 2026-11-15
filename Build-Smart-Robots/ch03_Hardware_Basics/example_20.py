# Run on the Raspberry Pi with the Arduino on USB
import time
import serial   # pip install pyserial

PORT = "/dev/ttyACM0"   # check with: ls /dev/tty*
link = serial.Serial(PORT, 115200, timeout=0.1)
time.sleep(2)           # Arduino resets on connect

def drive(left, right):
    msg = f"M,{int(left)},{int(right)}\n"
    link.write(msg.encode("ascii"))

try:
    t_end = time.monotonic() + 2.0
    while time.monotonic() < t_end:
        drive(120, 120)       # forward
        time.sleep(0.1)       # resend at 10 Hz
    drive(0, 0)
finally:
    drive(0, 0)
    link.close()
