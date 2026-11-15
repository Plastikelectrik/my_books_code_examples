robot = {"name": "Rover", "wheels": 2, "max_speed": 0.5}
print(robot["name"])
robot["battery"] = 87            # add a new key
robot["max_speed"] = 0.4         # change a value
for key, value in robot.items():
    print(f"{key:10s}: {value}")
print("has camera?", "camera" in robot)
print(robot.get("camera", "not installed"))
