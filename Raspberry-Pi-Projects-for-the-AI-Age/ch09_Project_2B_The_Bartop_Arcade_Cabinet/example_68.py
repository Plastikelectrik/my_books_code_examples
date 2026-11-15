# GPIO numbers we allow (2/3 are kept free for I2C,
# 0/1 for the HAT identification EEPROM)
AVAILABLE = set(range(4, 28))
KEYS = {"KEY_UP": 103, "KEY_DOWN": 108,
        "KEY_LEFT": 105, "KEY_RIGHT": 106,
        "KEY_LEFTCTRL": 29, "KEY_LEFTALT": 56,
        "KEY_SPACE": 57, "KEY_LEFTSHIFT": 42,
        "KEY_Z": 44, "KEY_X": 45, "KEY_1": 2, "KEY_5": 6}

player1 = {
    "UP": ("KEY_UP", 17),     "DOWN": ("KEY_DOWN", 27),
    "LEFT": ("KEY_LEFT", 22), "RIGHT": ("KEY_RIGHT", 23),
    "B1": ("KEY_LEFTCTRL", 5), "B2": ("KEY_LEFTALT", 6),
    "B3": ("KEY_SPACE", 13), "B4": ("KEY_LEFTSHIFT", 19),
    "B5": ("KEY_Z", 26),       "B6": ("KEY_X", 12),
    "START": ("KEY_1", 16),    "COIN": ("KEY_5", 20),
}

def check(mapping):
    used, errors = {}, []
    for name, (key, gpio) in mapping.items():
        if gpio not in AVAILABLE:
            errors.append(f"{name}: GPIO{gpio} not free")
        if gpio in used:
            errors.append(f"{name}: GPIO{gpio} twice")
        used[gpio] = name
    return errors

def overlay_line(name, key, gpio):
    return (f"dtoverlay=gpio-key,gpio={gpio},"
            f"active_low=1,gpio_pull=up,"
            f'keycode={KEYS[key]},label="P1_{name}"')

print("problems:", check(player1) or "none")
lines = [overlay_line(n, k, g)
         for n, (k, g) in player1.items()]
for name, (key, gpio) in list(player1.items())[:4]:
    print(f"P1_{name:6s} GPIO{gpio:<3d} -> {key}")
print(f"{len(lines)} overlay lines generated")
