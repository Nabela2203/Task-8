# 3. From the given list create two class Methods Area and Perimeter which will be going to calculate the Area
# and radius. -  Area of a circle = (πr)square. The perimeter of a circle = 2πr or pi d (d - distance).

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def Area(self):
        return math.pi * (self.radius ** 2)
    def Perimeter(self):
        return 2 * math.pi * self.radius

radii = [10, 501, 22, 37, 100, 999, 87, 351]
# normal
# for radius in radii
# print(radius)
circles = [Circle(radius) for radius in radii] # list comprehension

for circle in circles:
    print("Radius:", circle.radius)
    print("Area:", circle.Area())
    print("Perimeter:", circle.Perimeter())
    print() # space