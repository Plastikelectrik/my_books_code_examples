# Plot the training loss of the digit network
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.neural_network import MLPClassifier

d = load_digits()
net = MLPClassifier(hidden_layer_sizes=(64,),
                    max_iter=200, random_state=0)
net.fit(d.data / 16.0, d.target)

plt.figure(figsize=(5, 3))
plt.plot(net.loss_curve_)
plt.title("Training loss of a digit classifier")
plt.xlabel("iteration")
plt.ylabel("loss")
plt.tight_layout()
plt.savefig("loss_curve.png")
print("first loss:", round(net.loss_curve_[0], 3))
print("last loss :", round(net.loss_curve_[-1], 4))
