# Meaning of the bits returned by "vcgencmd get_throttled"
FLAGS = {
    0: "under-voltage now",
    1: "frequency capped now",
    2: "throttled now",
    3: "soft temperature limit now",
    16: "under-voltage has occurred",
    17: "frequency capping has occurred",
    18: "throttling has occurred",
    19: "soft temperature limit has occurred",
}

def decode_throttled(value):
    """Return a list of problems for a throttled value."""
    return [text for bit, text in FLAGS.items()
            if value & (1 << bit)]

for sample in ["0x0", "0x50000", "0x50005"]:
    problems = decode_throttled(int(sample, 16))
    print(sample)
    for p in problems or ["all good"]:
        print("   -", p)
