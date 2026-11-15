# Where is the gripper for given joint angles?
import math

L1, L2 = 0.30, 0.20   # link lengths in meters

def forward(theta1_deg, theta2_deg):
    t1 = math.radians(theta1_deg)
    t2 = math.radians(theta2_deg)
    x = L1 * math.cos(t1) + L2 * math.cos(t1 + t2)
    y = L1 * math.sin(t1) + L2 * math.sin(t1 + t2)
    return x, y

for angles in [(0, 0), (90, 0), (45, 45), (0, 90)]:
    x, y = forward(*angles)
    print(f"angles {angles}: x={x:.3f} m, y={y:.3f} m")
