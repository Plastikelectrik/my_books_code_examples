from gpiozero import Button
from evdev import UInput, ecodes as e
from signal import pause

MAP = {17: e.KEY_UP, 27: e.KEY_DOWN, 22: e.KEY_LEFT,
       23: e.KEY_RIGHT, 5: e.KEY_LEFTCTRL,
       6: e.KEY_LEFTALT, 13: e.KEY_SPACE,
       19: e.KEY_LEFTSHIFT, 26: e.KEY_Z, 12: e.KEY_X,
       16: e.KEY_1, 20: e.KEY_5}

ui = UInput({e.EV_KEY: list(MAP.values())},
            name="arcade-panel-p1")

def make_handler(code, value):
    def handler():
        ui.write(e.EV_KEY, code, value)  # 1 down, 0 up
        ui.syn()
    return handler

buttons = []
for gpio, code in MAP.items():
    b = Button(gpio, pull_up=True, bounce_time=0.005)
    b.when_pressed = make_handler(code, 1)
    b.when_released = make_handler(code, 0)
    buttons.append(b)

print("Arcade panel ready")
pause()
