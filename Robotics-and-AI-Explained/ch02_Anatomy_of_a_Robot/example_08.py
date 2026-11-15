# Count the DOF of robots described by their joints
robots = {
    "vacuum": ["wheel", "wheel"],
    "scara": ["rev", "rev", "pris", "rev"],
    "arm6": ["rev"] * 6,
    "cobot7": ["rev"] * 7,
}
for name, joints in robots.items():
    rev = joints.count("rev")
    pris = joints.count("pris")
    print(f"{name:7s}: {len(joints)} DOF "
          f"({rev} revolute, {pris} prismatic)")
