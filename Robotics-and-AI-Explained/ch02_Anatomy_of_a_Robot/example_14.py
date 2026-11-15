# A simple class that combines robot parts
class Robot:
    def __init__(self, name, battery_wh, power_w):
        self.name = name
        self.battery_wh = battery_wh
        self.power_w = power_w
        self.distance = 0.0

    def drive(self, meters, hours):
        used = self.power_w * hours
        if used > self.battery_wh:
            print(self.name, "cannot finish: low battery")
            return
        self.battery_wh -= used
        self.distance += meters
        print(f"{self.name} drove {meters} m, "
              f"battery left {self.battery_wh:.1f} Wh")

r = Robot("Scout", battery_wh=59.2, power_w=32.5)
r.drive(200, hours=0.5)
r.drive(300, hours=1.0)
r.drive(100, hours=0.5)
print("total distance:", r.distance, "m")
