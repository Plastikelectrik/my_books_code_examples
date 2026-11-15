# Months until a robot investment is paid back
investment = 85_000     # robot, integration, training
monthly_costs = 900     # maintenance, software, energy
hours_saved_month = 300      # person-hours of task work
hourly_cost = 28.0           # full labor cost per hour

monthly_saving = hours_saved_month * hourly_cost
net_monthly = monthly_saving - monthly_costs
months = investment / net_monthly
print(f"monthly saving: {monthly_saving:,.0f}")
print(f"net per month : {net_monthly:,.0f}")
print(f"payback       : {months:.1f} months")
