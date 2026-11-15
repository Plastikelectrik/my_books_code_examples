# Learn rules to decide if a robot should recharge
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text

# features: battery %, distance to charger (m), busy (0/1)
X = [[80, 10, 1], [15, 5, 0], [30, 50, 0], [10, 40, 1],
     [60, 30, 0], [25, 5, 1], [90, 60, 0], [20, 20, 0],
     [35, 80, 1], [50, 15, 1], [12, 70, 0], [70, 5, 0]]
y = [0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0]   # 1 = recharge

tree = DecisionTreeClassifier(max_depth=2, random_state=0)
tree.fit(X, y)
names = ["battery", "distance", "busy"]
print(export_text(tree, feature_names=names))
print("decision for [28, 60, 0]:",
      tree.predict([[28, 60, 0]]))
