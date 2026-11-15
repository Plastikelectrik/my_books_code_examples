MODES = {"0": "stop", "1": "SD card", "2": "network",
         "3": "RPIBOOT", "4": "USB storage",
         "5": "BCM USB storage", "6": "NVMe",
         "7": "HTTP", "e": "stop", "f": "restart"}

def decode(order):
    digits = order.lower().removeprefix("0x")
    return [MODES.get(d, "?") for d in reversed(digits)]

for value in ["0xf41", "0xf416", "0xf461"]:
    print(f"{value:7s}:", " -> ".join(decode(value)))
