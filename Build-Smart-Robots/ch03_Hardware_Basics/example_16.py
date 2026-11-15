# Runs ON the ESP32 (save as main.py on the board)
from machine import Pin
import time

led = Pin(2, Pin.OUT)   # GPIO 2: on-board LED
count = 0               # on many dev boards
while True:
    led.value(not led.value())
    count += 1
    print("toggle", count)
    time.sleep(0.5)
