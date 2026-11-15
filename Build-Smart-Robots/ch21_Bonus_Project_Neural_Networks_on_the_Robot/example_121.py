from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

d = load_digits()
Xtr, Xte, ytr, yte = train_test_split(
    d.data / 16.0, d.target, test_size=0.25,
    random_state=0)
mlp = MLPClassifier(hidden_layer_sizes=(32,),
                    max_iter=1000, random_state=0)
mlp.fit(Xtr, ytr)
print(f"test accuracy: {mlp.score(Xte, yte):.3f}")
print("parameters:",
      sum(w.size for w in mlp.coefs_)
      + sum(b.size for b in mlp.intercepts_))
