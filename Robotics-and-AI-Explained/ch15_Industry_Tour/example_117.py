# Simple fleet sizing for goods-to-person picking
orders_per_hour = 1800        # order lines per hour
lines_per_trip = 3        # lines picked per shelf trip
trip_minutes = 4.0            # drive, wait, return
utilization = 0.80            # robots are busy 80%
charging_share = 0.15         # 15% of robots charging

trips = orders_per_hour / lines_per_trip
trips_per_robot = 60 / trip_minutes * utilization
working = trips / trips_per_robot
total = working / (1 - charging_share)
print(f"trips per hour   : {trips:.0f}")
print(f"robots working   : {working:.1f}")
print(f"robots incl. charging: {total:.0f}")
