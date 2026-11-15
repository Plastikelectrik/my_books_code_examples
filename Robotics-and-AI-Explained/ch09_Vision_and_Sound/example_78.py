# Find the dominant frequency in a noisy signal
import numpy as np

sr = 16000
t = np.arange(0, 1.0, 1 / sr)
rng = np.random.default_rng(2)
signal = (0.6 * np.sin(2 * np.pi * 2900 * t)
          + 0.2 * np.sin(2 * np.pi * 300 * t)
          + rng.normal(0, 0.3, len(t)))
spectrum = np.abs(np.fft.rfft(signal))
freqs = np.fft.rfftfreq(len(signal), 1 / sr)
top = freqs[np.argsort(spectrum)[-2:]][::-1]
print("strongest frequencies (Hz):", top.round())
if abs(top[0] - 2900) < 50:
    print("smoke alarm tone detected")
