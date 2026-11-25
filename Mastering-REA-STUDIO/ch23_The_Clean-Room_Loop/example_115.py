import os
import sys

TEAS = [("green", 80, 120), ("black", 95, 240),
        ("oolong", 90, 180), ("herbal", 100, 300)]


def parse_strength(text):
    s = text.lstrip(" \t\n\v\f\r")
    sign = 1
    if s[:1] in ("+", "-"):
        sign = -1 if s[0] == "-" else 1
        s = s[1:]
    digits = ""
    for ch in s:
        if ch not in "0123456789":
            break
        digits += ch
    return sign * int(digits) if digits else 0


def check(name):
    h = 7
    for b in os.fsencode(name):
        h = (h * 31 + b) % 2**32
    return h % 10007


def main(argv):
    if len(argv) < 2:
        print("usage: kettle TEA [STRENGTH]")
        return 1
    strength = 3
    if len(argv) > 2:
        strength = parse_strength(argv[2])
    if strength < 1 or strength > 5:
        print("error: strength must be 1-5")
        return 2
    for name, temp, base in TEAS:
        if name == argv[1]:
            t = base + (strength - 3) * 20
            if temp < 85:
                t += (85 - temp) * 2
            t = max(t, 30)
            c = check(name)
            print(f"{name} {temp}C {t}s check={c}")
            return 0
    print(f"error: unknown tea '{argv[1]}'")
    return 3


if __name__ == "__main__":
    sys.exit(main(sys.argv))
