import numpy as np

def window_features(z, fs=100):
    z = z - z.mean()
    std = z.std()
    p2p = z.max() - z.min()
    kurt = np.mean(z ** 4) / (std ** 4 + 1e-12)
    spectrum = np.abs(np.fft.rfft(z))
    freqs = np.fft.rfftfreq(len(z), 1 / fs)
    dom = freqs[1:][np.argmax(spectrum[1:])]
    zcr = np.mean(np.abs(np.diff(np.sign(z)))) / 2
    return [std, p2p, kurt, dom, zcr]

def make_dataset(data, win=100):
    X, y = [], []
    for label, z in data.items():
        for i in range(0, len(z) - win + 1, win):
            X.append(window_features(z[i:i + win]))
            y.append(label)
    return np.array(X), np.array(y)

if __name__ == "__main__":
    data = dict(np.load("terrain.npz"))
    X, y = make_dataset(data)
    print("dataset:", X.shape)
    print("labels:", sorted(set(y.tolist())))
    np.savez("features.npz", X=X, y=y)
