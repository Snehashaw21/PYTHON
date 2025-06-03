#Calculate surface area of a cylinder

import math

r = float(input("Radius: "))
h = float(input("Height: "))

area = 2 * math.pi * r * (r + h)

print("Surface area =", round(area, 2))
