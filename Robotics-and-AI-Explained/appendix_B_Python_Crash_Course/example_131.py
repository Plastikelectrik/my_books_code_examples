robot_name = "Rover"        # text (str)
wheels = 2                  # whole number (int)
speed = 0.35                # decimal number (float)
is_moving = True            # truth value (bool)

print(robot_name, "has", wheels, "wheels")
print("speed in m/s:", speed)
print("type of speed:", type(speed).__name__)
print("moving?", is_moving)
