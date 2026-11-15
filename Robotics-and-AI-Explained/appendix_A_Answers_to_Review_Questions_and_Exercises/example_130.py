investment, monthly_costs, rate = 85_000, 900, 28.0
for hours in [100, 150, 200, 250, 300]:
    net = hours * rate - monthly_costs
    print(f"{hours} h/month -> payback "
          f"{investment / net:5.1f} months")
