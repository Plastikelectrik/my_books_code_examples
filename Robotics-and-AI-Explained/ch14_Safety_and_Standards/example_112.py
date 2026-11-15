# Detect a faulty sensor and use the agreeing majority
def vote(a, b, c, tolerance=0.05):
    pairs = [(a, b), (a, c), (b, c)]
    agree = [(x, y) for x, y in pairs
             if abs(x - y) <= tolerance]
    if not agree:
        return None, "no agreement -> SAFE STOP"
    x, y = agree[0]
    return (x + y) / 2, "ok"

readings = [(1.20, 1.21, 1.19),     # all agree
            (1.20, 1.22, 0.30),     # one faulty
            (1.20, 0.80, 0.30)]     # no agreement
for r in readings:
    value, status = vote(*r)
    print(r, "->", value if value is None
          else round(value, 3), status)
