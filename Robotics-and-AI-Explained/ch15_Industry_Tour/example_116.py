# OEE of a robot cell during one shift
planned_min = 480           # 8-hour shift
downtime_min = 45           # stops and changeovers
ideal_cycle_s = 30          # seconds per part at best
parts_made = 780
good_parts = 760

run_min = planned_min - downtime_min
availability = run_min / planned_min
performance = (parts_made * ideal_cycle_s / 60) / run_min
quality = good_parts / parts_made
oee = availability * performance * quality
print(f"availability: {availability:.1%}")
print(f"performance : {performance:.1%}")
print(f"quality     : {quality:.1%}")
print(f"OEE         : {oee:.1%}")
