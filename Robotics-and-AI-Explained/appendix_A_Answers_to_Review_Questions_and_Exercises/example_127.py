class Robot:
    def __init__(self, name, capacity_wh):
        self.name = name
        self.capacity_wh = capacity_wh
        self.energy_wh = capacity_wh

    def use(self, wh):
        self.energy_wh = max(0.0, self.energy_wh - wh)

    def charge(self, wh):
        self.energy_wh = min(self.capacity_wh,
                             self.energy_wh + wh)

bot = Robot("Rover", capacity_wh=60)
bot.use(45)
print("after driving :", bot.energy_wh, "Wh")
bot.charge(100)
print("after charging:", bot.energy_wh, "Wh")
