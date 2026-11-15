import numpy as np
import cv2
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

rng = np.random.default_rng(0)
NAMES = ["circle", "square", "triangle"]

def make_shape(kind):
    img = np.zeros((100, 100), np.uint8)
    cx, cy = rng.integers(35, 65, 2)
    s = int(rng.integers(15, 30))
    a = rng.uniform(0, np.pi)
    if kind == 0:
        cv2.circle(img, (int(cx), int(cy)), s, 255, -1)
    else:
        n = 4 if kind == 1 else 3
        ang = a + np.arange(n) * 2 * np.pi / n
        pts = np.stack([cx + s * np.cos(ang),
                        cy + s * np.sin(ang)], 1)
        cv2.fillPoly(img, [pts.astype(np.int32)], 255)
    noise = rng.random(img.shape) < 0.02
    img[noise] = 255 - img[noise]
    return cv2.medianBlur(img, 3)

def features(img):
    cs, _ = cv2.findContours(img, cv2.RETR_EXTERNAL,
                             cv2.CHAIN_APPROX_SIMPLE)
    c = max(cs, key=cv2.contourArea)
    area = cv2.contourArea(c)
    per = cv2.arcLength(c, True)
    circ = 4 * np.pi * area / (per * per)
    corners = len(cv2.approxPolyDP(c, 0.04 * per,
                                   True))
    hull = cv2.contourArea(cv2.convexHull(c))
    x, y, w, h = cv2.boundingRect(c)
    return [circ, corners, area / hull,
            area / (w * h)]

X, y = [], []
for i in range(600):
    kind = i % 3
    X.append(features(make_shape(kind)))
    y.append(kind)
X, y = np.array(X), np.array(y)

Xtr, Xte, ytr, yte = train_test_split(
    X, y, test_size=0.25, random_state=0)
clf = RandomForestClassifier(n_estimators=100,
                             random_state=0)
clf.fit(Xtr, ytr)
print(classification_report(yte, clf.predict(Xte),
                            target_names=NAMES))

# Which features matter most?
names = ["circularity", "corners", "solidity", "extent"]
for n, imp in sorted(zip(names,
                         clf.feature_importances_),
                     key=lambda t: -t[1]):
    print(f"{n:12s} {imp:.2f}")
