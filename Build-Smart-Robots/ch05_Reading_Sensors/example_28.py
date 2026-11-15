# Runs ON the ESP32. IMU: SDA->GPIO21, SCL->GPIO22
from machine import Pin, I2C
import time

i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
ADDR = 0x68
i2c.writeto_mem(ADDR, 0x6B, b"\x00")   # wake up

def read_word(reg):
    hi, lo = i2c.readfrom_mem(ADDR, reg, 2)
    v = (hi << 8) | lo
    return v - 65536 if v > 32767 else v

GZ_REG = 0x47          # gyro Z, high byte
SCALE = 131.0          # LSB per deg/s (default)

print("Keep still: measuring gyro offset...")
offset = sum(read_word(GZ_REG) for _ in range(200))
offset /= 200

heading = 0.0
last = time.ticks_ms()
while True:
    now = time.ticks_ms()
    dt = time.ticks_diff(now, last) / 1000
    last = now
    rate = (read_word(GZ_REG) - offset) / SCALE
    heading += rate * dt     # integrate deg/s
    print("G,{:.1f},{:.1f}".format(rate, heading))
    time.sleep(0.02)
