# Inspect one 8x8 handwritten digit as numbers
from sklearn.datasets import load_digits

digits = load_digits()
print("images:", digits.images.shape)
print("label of first image:", digits.target[0])
for row in digits.images[0]:
    print(" ".join(f"{int(v):2d}" for v in row))
