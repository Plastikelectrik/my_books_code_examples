import pybullet as p
import pybullet_data
import numpy as np

p.connect(p.DIRECT)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
arm = p.loadURDF("kuka_iiwa/model.urdf",
                 useFixedBase=True)
n = p.getNumJoints(arm)
HAND = n - 1                     # last link
target = [0.5, 0.2, 0.4]         # meters
for it in range(20):             # refine iteratively
    angles = p.calculateInverseKinematics(
        arm, HAND, target, maxNumIterations=100)
    for j in range(n):
        p.resetJointState(arm, j, angles[j])
    hand = p.getLinkState(arm, HAND)[4]
    if np.linalg.norm(np.array(hand) - target) < 1e-3:
        break
err = np.linalg.norm(np.array(hand) - target)
print("joints:", n, "| refinements:", it + 1)
print("angles (deg):",
      np.round(np.degrees(angles), 0).astype(int))
print("hand at:", np.round(hand, 3),
      f"error {1000 * err:.1f} mm")
p.disconnect()
