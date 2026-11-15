import math

x = 0.1 + 0.2
print("x =", x)
print("x == 0.3 ?", x == 0.3)
print("isclose  ?", math.isclose(x, 0.3))
position, goal = 2.9999999, 3.0
print("arrived  ?", abs(position - goal) < 0.01)
