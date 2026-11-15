# Shares and growth from IFR World Robotics 2026 data
world_2025 = 603_000
china_2025 = 354_000
usa_2025 = 38_400
forecast = {2025: 603_000, 2026: 655_000, 2029: 806_000}

print(f"China share: {china_2025 / world_2025:.0%}")
print(f"USA share  : {usa_2025 / world_2025:.1%}")
years = 2029 - 2026
ratio = forecast[2029] / forecast[2026]
cagr = ratio ** (1 / years) - 1
print(f"growth 2026-2029: {cagr:.1%} per year")
growth = forecast[2026] / forecast[2025] - 1
print(f"growth 2025-2026: {growth:.1%}")
