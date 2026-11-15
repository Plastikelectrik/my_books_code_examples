import math

def gait(direction="forward", turn=0.0, period=1.2):
    foot_phase = 90 if direction == "forward" else -90
    hip_l = 25 * (1 + turn)          # turn: -1 .. 1
    hip_r = 25 * (1 - turn)
    return {"period": period,
            "hip_L": (90, hip_l, 0),
            "hip_R": (90, hip_r, 0),
            "foot_L": (90, 20, foot_phase),
            "foot_R": (90, 20, foot_phase)}

for name, g in [("forward", gait()),
                ("backward", gait("backward")),
                ("turn right", gait(turn=0.5))]:
    print(f"{name:10s} hip amplitudes L/R: "
          f"{g['hip_L'][1]:4.1f} / {g['hip_R'][1]:4.1f}, "
          f"foot phase {g['foot_L'][2]:+d}")
