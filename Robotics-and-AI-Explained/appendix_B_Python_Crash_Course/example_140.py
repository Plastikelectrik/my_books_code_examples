class Robot:
    def __init__(self, name, x=0.0):
        self.name = name
        self.x = x

    def move(self, dx):
        self.x += dx
        return self.x

    def __str__(self):
        return f"{self.name} at x={self.x:.1f} m"

a = Robot("Ada")
b = Robot("Bo", x=5.0)
a.move(1.5)
b.move(-2.0)
print(a)
print(b)
