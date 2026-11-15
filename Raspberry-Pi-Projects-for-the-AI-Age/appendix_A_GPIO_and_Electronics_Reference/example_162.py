def divider(vin, r1, r2):
    return vin * r2 / (r1 + r2)

for r1, r2 in [(10_000, 18_000), (2_200, 3_300),
               (4_700, 10_000)]:
    v = divider(5.0, r1, r2)
    ok = "safe" if v <= 3.3 else "TOO HIGH"
    print(f"R1={r1:6d} R2={r2:6d} -> {v:.2f} V ({ok})")
