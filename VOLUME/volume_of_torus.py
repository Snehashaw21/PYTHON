#Calculate volume of the toru

import math

R = float(input("Enter the major radius (R): "))
r = float(input("Enter the minor radius (r): "))

volume = 2 * math.pi**2 * R * r**2

print("Volume of the torus is:", volume)
