# Compare broadcast spraying with spot spraying
field_ha = 40
liters_per_ha = 2.0            # broadcast dose
weed_cover = 0.12              # 12% of area has weeds
detection_rate = 0.95          # weeds found by camera
false_spray = 0.03             # extra area sprayed

broadcast = field_ha * liters_per_ha
spot_area = weed_cover * detection_rate + false_spray
spot = field_ha * liters_per_ha * spot_area
missed = weed_cover * (1 - detection_rate)
print(f"broadcast: {broadcast:.0f} L")
print(f"spot     : {spot:.1f} L "
      f"({1 - spot / broadcast:.0%} less)")
print(f"weed area missed: {missed:.1%} of field")
