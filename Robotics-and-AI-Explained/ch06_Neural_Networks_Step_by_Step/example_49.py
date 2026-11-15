# Train and test an MLP classifier on 8x8 digit images
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix

digits = load_digits()
X = digits.data / 16.0           # scale to 0..1
y = digits.target
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.25, random_state=0)

net = MLPClassifier(hidden_layer_sizes=(64,),
                    max_iter=400, random_state=0)
net.fit(X_tr, y_tr)
print(f"test accuracy: {net.score(X_te, y_te):.3f}")
cm = confusion_matrix(y_te, net.predict(X_te))
errors = [(i, j, int(cm[i, j])) for i in range(10)
          for j in range(10) if i != j and cm[i, j] > 1]
print("most common confusions (true, pred, n):")
for e in sorted(errors, key=lambda e: -e[2])[:3]:
    print("  ", e)
