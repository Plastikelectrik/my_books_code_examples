# A 9 Hz vibration sampled at 10 Hz looks like 1 Hz
import numpy as np

f_signal = 9.0                  # real vibration (Hz)
for fs in [100.0, 10.0]:        # sample rates (Hz)
    t = np.arange(0, 2, 1 / fs)
    x = np.sin(2 * np.pi * f_signal * t)
    spectrum = np.abs(np.fft.rfft(x))
    freqs = np.fft.rfftfreq(len(x), 1 / fs)
    seen = freqs[spectrum.argmax()]
    print(f"sampled at {fs:5.1f} Hz -> looks like "
          f"{seen:.1f} Hz")
