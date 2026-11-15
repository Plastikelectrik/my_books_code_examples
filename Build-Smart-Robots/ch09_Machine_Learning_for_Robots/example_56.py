import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix

rng = np.random.default_rng(3)
t = np.arange(6000) / 100

def noisy_sine(amp, freq, noise):
    return amp * np.sin(2 * np.pi * freq * t) \
        + rng.normal(0, noise, t.size)

data = {"floor": noisy_sine(0.03, 18, 0.02),
        "carpet": noisy_sine(0.015, 9, 0.015),
        "rug": noisy_sine(0.016, 10, 0.016)}

def feats(z):
    z = z - z.mean()
    s = np.abs(np.fft.rfft(z))
    fr = np.fft.rfftfreq(len(z), 0.01)
    return [z.std(), z.max() - z.min(),
            fr[1:][np.argmax(s[1:])]]

X, y = [], []
for lab, z in data.items():
    for i in range(0, 6000, 100):
        X.append(feats(z[i:i + 100]))
        y.append(lab)
labels = list(data)
pred = cross_val_predict(
    RandomForestClassifier(random_state=0), X, y, cv=5)
print("rows = true, columns = predicted")
print(labels)
print(confusion_matrix(y, pred, labels=labels))
