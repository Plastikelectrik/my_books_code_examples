# Shuffle and split a dataset with scikit-learn
import numpy as np
from sklearn.model_selection import train_test_split

X = np.arange(20).reshape(10, 2)  # 10 rows, 2 cols
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)
print("training examples:", len(X_train))
print("test examples    :", len(X_test))
print("test labels      :", y_test)
