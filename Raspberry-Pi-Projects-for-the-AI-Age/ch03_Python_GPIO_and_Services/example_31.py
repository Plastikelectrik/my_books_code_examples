from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(2)  # internal pull-up, press = ground

button.when_pressed = led.on
button.when_released = led.off
print("Press the button. Ctrl+C to stop.")
pause()                     # keep the program running
