import math
import pybullet as p
import pybullet_data

p.connect(p.DIRECT)              # p.GUI for a window
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)
p.loadURDF("plane.urdf")
bot = p.loadURDF("rover.urdf", [0, 0, 0.04])
LEFT, RIGHT = 0, 1               # joint indices
R, L = 0.033, 0.15               # wheel radius, base
# make the caster slippery (it should roll freely)
p.changeDynamics(bot, 2, lateralFriction=0.0)

def drive(v, w):
    wl = (v - w * L / 2) / R     # rad/s
    wr = (v + w * L / 2) / R
    p.setJointMotorControl2(bot, LEFT,
        p.VELOCITY_CONTROL, targetVelocity=wl, force=0.5)
    p.setJointMotorControl2(bot, RIGHT,
        p.VELOCITY_CONTROL, targetVelocity=wr, force=0.5)

def pose():
    pos, orn = p.getBasePositionAndOrientation(bot)
    yaw = p.getEulerFromQuaternion(orn)[2]
    return pos[0], pos[1], yaw

goal = (1.0, 0.5)
dt = 1 / 240
for step in range(240 * 20):     # up to 20 s
    if step % 12 == 0:           # control at 20 Hz
        x, y, th = pose()
        dx, dy = goal[0] - x, goal[1] - y
        dist = math.hypot(dx, dy)
        if dist < 0.03:
            break
        err = math.atan2(dy, dx) - th
        err = math.atan2(math.sin(err), math.cos(err))
        v = min(0.25, dist) * max(0.0, math.cos(err))
        drive(v, 2.0 * err)
    p.stepSimulation()
drive(0, 0)
x, y, th = pose()
print(f"stopped at ({x:.2f}, {y:.2f}) after "
      f"{step * dt:.1f} s, goal {goal}")
p.disconnect()
