WHEELBASE_M = 0.15

def forward_kin(v_left, v_right, L=WHEELBASE_M):
    v = (v_right + v_left) / 2
    w = (v_right - v_left) / L
    return v, w

def inverse_kin(v, w, L=WHEELBASE_M):
    return v - w * L / 2, v + w * L / 2

v, w = forward_kin(0.1, 0.2)
print(f"wheels (0.1, 0.2) -> v={v:.2f}, w={w:.2f}")
vl, vr = inverse_kin(0.15, 0.6667)
print(f"want v=0.15, w=0.67 -> wheels "
      f"({vl:.3f}, {vr:.3f})")
r = 0.15 / 0.6667
print(f"turning radius: {r:.3f} m")
