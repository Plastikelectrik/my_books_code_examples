# Estimate direction from the delay between two mics
import numpy as np

sr, D, c = 48000, 0.20, 343.0      # rate, mic gap, speed
rng = np.random.default_rng(4)
clap = rng.normal(0, 1, 400)       # a short noisy sound

true_angle = 30.0
delay_s = D * np.sin(np.radians(true_angle)) / c
shift = int(round(delay_s * sr))
left = np.concatenate([clap, np.zeros(100)])
right = np.concatenate([np.zeros(shift), clap,
                        np.zeros(100 - shift)])

corr = np.correlate(right, left, mode="full")
lag = corr.argmax() - (len(left) - 1)
est = np.degrees(np.arcsin(lag / sr * c / D))
print("delay in samples:", lag)
print(f"estimated direction: {est:.1f} deg "
      f"(true {true_angle} deg)")
