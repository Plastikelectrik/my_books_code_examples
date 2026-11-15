HARD = {0, 4}                    # hard left / right

def reward(offset, a):
    if abs(offset) > 1.0:
        return -10.0
    r = 1.0 - 2.0 * abs(offset)
    if a in HARD:
        r -= 1.0                 # discourage zigzag
    return r

# ... and in run_episode():  r = reward(offset, a)
