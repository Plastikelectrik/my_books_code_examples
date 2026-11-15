from sklearn.datasets import load_digits

digits = load_digits()
X, y = digits.data, digits.target
print("images:", X.shape, "labels:", y.shape)
print("label of the first image:", y[0])
img = digits.images[0]
for row in img:
    print("".join("#" if v > 8 else
                  "+" if v > 3 else "." for v in row))
