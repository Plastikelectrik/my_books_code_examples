import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier

f = np.load("features.npz")
model = RandomForestClassifier(n_estimators=100,
                               random_state=0)
model.fit(f["X"], f["y"])
joblib.dump(model, "terrain_model.joblib")

# --- later, on the robot ---
robot_model = joblib.load("terrain_model.joblib")
one_window = f["X"][0:1]          # 1 x 5 features
print("predicted surface:",
      robot_model.predict(one_window)[0])
