import time

class Executor:
    def __init__(self, send):
        self.send = send             # function(v, w)
        self.v = self.w = 0.0
        self.until = 0.0

    def handle(self, cmd, now):
        kind = cmd[0]
        if kind == "stop":
            self.v = self.w = 0.0
            self.until = 0.0
        elif kind == "drive":
            _, self.v, self.w, dur = cmd
            self.until = now + dur

    def tick(self, now):
        if now >= self.until:
            self.v = self.w = 0.0
        self.send(self.v, self.w)

if __name__ == "__main__":
    log = []
    ex = Executor(lambda v, w: log.append((v, w)))
    t = 0.0
    schedule = {0.0: ("drive", 0.12, 0.0, 3.0),
                1.0: ("stop",),
                2.0: ("drive", 0.0, 1.0, 1.0)}
    for step in range(40):                # 4 s at 10 Hz
        t = round(step * 0.1, 1)
        if t in schedule:
            ex.handle(schedule[t], t)
        ex.tick(t)
    for k in [0, 5, 10, 15, 20, 25, 30, 35]:
        print(f"t={k/10:.1f}s  v={log[k][0]:.2f} "
              f"w={log[k][1]:.1f}")
