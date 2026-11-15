# Simulate a differential-drive robot for a few seconds
import math

WHEEL_BASE = 0.30     # meters between the wheels
x, y, heading = 0.0, 0.0, 0.0   # pose: position + angle
dt = 0.1              # time step in seconds

def step(v_left, v_right):
    global x, y, heading
    v = (v_right + v_left) / 2
    w = (v_right - v_left) / WHEEL_BASE
    x += v * math.cos(heading) * dt
    y += v * math.sin(heading) * dt
    heading += w * dt

for _ in range(20):          # 2 s straight
    step(0.5, 0.5)
print(f"straight: x={x:.2f} y={y:.2f} "
      f"heading={math.degrees(heading):.0f} deg")
for _ in range(20):          # 2 s curve to the left
    step(0.3, 0.5)
print(f"curve:    x={x:.2f} y={y:.2f} "
      f"heading={math.degrees(heading):.0f} deg")
for _ in range(10):          # 1 s turn on the spot
    step(-0.2, 0.2)
print(f"spin:     x={x:.2f} y={y:.2f} "
      f"heading={math.degrees(heading):.0f} deg")
