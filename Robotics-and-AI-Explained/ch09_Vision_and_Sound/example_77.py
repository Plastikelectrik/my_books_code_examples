# Synthesize a tone and measure its loudness
import numpy as np

sr = 16000                         # samples per second
t = np.arange(0, 0.5, 1 / sr)      # half a second
for amp in [1.0, 0.5, 0.1]:
    wave = amp * np.sin(2 * np.pi * 440 * t)
    rms = np.sqrt(np.mean(wave ** 2))
    db = 20 * np.log10(rms)
    print(f"amplitude {amp:.1f}: RMS {rms:.3f}, "
          f"{db:6.1f} dBFS")
print("samples in 0.5 s:", len(t))
