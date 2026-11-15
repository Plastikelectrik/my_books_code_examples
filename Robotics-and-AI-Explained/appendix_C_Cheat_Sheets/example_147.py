from collections import deque

def clamp(x, lo, hi):
    return max(lo, min(hi, x))

def map_range(x, in_lo, in_hi, out_lo, out_hi):
    k = (x - in_lo) / (in_hi - in_lo)
    return out_lo + k * (out_hi - out_lo)

class MovingAverage:
    def __init__(self, n):
        self.buf = deque(maxlen=n)

    def add(self, x):
        self.buf.append(x)
        return sum(self.buf) / len(self.buf)

print(clamp(15, -12, 12))
print(map_range(512, 0, 1023, 0, 5.0))
ma = MovingAverage(3)
print([round(ma.add(v), 1) for v in [10, 12, 30, 11]])
