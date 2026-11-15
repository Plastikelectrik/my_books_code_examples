import numpy as np

RATE, FRAME = 16000, 480          # 30 ms frames at 16 kHz
rng = np.random.default_rng(3)

# Test signal: 1 s silence, 1.2 s "speech", 0.8 s silence
t = np.arange(int(1.2 * RATE)) / RATE
speech = (0.30 * np.sin(2 * np.pi * 180 * t)
          * (0.6 + 0.4 * np.sin(2 * np.pi * 3 * t)))
signal = np.concatenate([np.zeros(RATE), speech,
                         np.zeros(int(0.8 * RATE))])
signal += rng.normal(0, 0.01, signal.size)  # noise

def frame_energy(x):
    n = x.size // FRAME
    frames = x[:n * FRAME].reshape(n, FRAME)
    return np.sqrt((frames ** 2).mean(axis=1))   # RMS

def detect(energy, factor=4.0, hang=10):
    noise = np.median(energy[:20])       # first 0.6 s
    active = energy > noise * factor
    segments, start, quiet = [], None, 0
    for i, a in enumerate(active):
        if a:
            start = i if start is None else start
            quiet = 0
        elif start is not None:
            quiet += 1
            if quiet > hang:             # 300 ms silence
                segments.append((start, i - quiet))
                start, quiet = None, 0
    return segments, noise

e = frame_energy(signal)
segs, noise = detect(e)
print(f"frames: {e.size}, noise RMS: {noise:.4f}")
for s, f in segs:
    print(f"speech from {s*FRAME/RATE:.2f} s "
          f"to {(f+1)*FRAME/RATE:.2f} s")
