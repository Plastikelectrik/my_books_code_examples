def debounce(samples, stable_ms=5):
    """Return the times (ms) of clean presses.
    samples: 0/1 pin readings, one per ms."""
    presses, state, count = [], 0, 0
    for t, s in enumerate(samples):
        count = count + 1 if s != state else 0
        if count >= stable_ms:  # new state is stable
            state, count = s, 0
            if state == 1:
                presses.append(t)
    return presses

# One real press with bouncing, then a short glitch
noisy = [0]*5 + [1,0,1,0,1,1,1,1,1,1,1,1] + [0]*10 \
        + [1,0] + [0]*10
print("raw rising edges:", sum(1 for a, b in
      zip(noisy, noisy[1:]) if a == 0 and b == 1))
print("clean presses at ms:", debounce(noisy))
