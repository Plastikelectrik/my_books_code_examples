import math
import random
import pybullet as p
import pybullet_data

R, L = 0.033, 0.15

def trial(friction, mass, max_force):
    p.connect(p.DIRECT)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0, 0, -9.81)
    plane = p.loadURDF("plane.urdf")
    bot = p.loadURDF("rover.urdf", [0, 0, 0.04])
    p.changeDynamics(plane, -1, lateralFriction=friction)
    p.changeDynamics(bot, -1, mass=mass)
    p.changeDynamics(bot, 2, lateralFriction=0.0)
    goal, t = (1.0, 0.5), None
    for step in range(240 * 20):
        if step % 12 == 0:
            pos, orn = \
                p.getBasePositionAndOrientation(bot)
            th = p.getEulerFromQuaternion(orn)[2]
            dx, dy = goal[0] - pos[0], goal[1] - pos[1]
            dist = math.hypot(dx, dy)
            if dist < 0.03:
                t = step / 240
                break
            err = math.atan2(dy, dx) - th
            err = math.atan2(math.sin(err), math.cos(err))
            v = min(0.25, dist) * max(0.0, math.cos(err))
            w = 2.0 * err
            for j, s in ((0, -1), (1, 1)):
                p.setJointMotorControl2(
                    bot, j, p.VELOCITY_CONTROL,
                    targetVelocity=(v + s * w * L / 2)
                    / R,
                    force=max_force)
        p.stepSimulation()
    p.disconnect()
    return t

random.seed(0)
for k in range(6):
    fr = random.uniform(0.02, 1.0)      # floor grip
    m = random.uniform(0.8, 3.0)        # robot mass kg
    f = random.uniform(0.005, 0.08)     # motor strength
    t = trial(fr, m, f)
    res = f"{t:.1f} s" if t else "FAILED (timeout)"
    print(f"friction {fr:.2f} mass {m:.2f} kg "
          f"force {f:.2f} -> {res}")
