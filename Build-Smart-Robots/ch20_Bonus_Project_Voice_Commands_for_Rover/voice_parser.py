SPEEDS = [0.08, 0.12, 0.18]          # m/s levels

class CommandParser:
    def __init__(self):
        self.level = 1               # start medium

    def parse(self, text):
        words = text.lower().split()
        if not words or words[0] != "rover":
            return ("ignore",)
        cmd = " ".join(words[1:])
        v = SPEEDS[self.level]
        if cmd == "stop":
            return ("stop",)
        if cmd == "forward":
            return ("drive", v, 0.0, 3.0)
        if cmd == "back":
            return ("drive", -v, 0.0, 1.5)
        if cmd == "left":
            return ("drive", 0.0, 1.0, 1.0)
        if cmd == "right":
            return ("drive", 0.0, -1.0, 1.0)
        if cmd == "faster":
            self.level = min(self.level + 1,
                             len(SPEEDS) - 1)
            return ("speed", SPEEDS[self.level])
        if cmd == "slower":
            self.level = max(self.level - 1, 0)
            return ("speed", SPEEDS[self.level])
        if cmd == "come home":
            return ("mission", "home")
        return ("unknown", cmd)

if __name__ == "__main__":
    p = CommandParser()
    tests = ["rover forward", "turn left please",
             "rover faster", "rover forward",
             "rover left", "rover stop", "rover dance"]
    for t in tests:
        print(f"{t!r:22} -> {p.parse(t)}")
