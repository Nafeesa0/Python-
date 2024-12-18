import math
from pack_main import rect
from pack_main import circle
from pack_main.pack_sub import cuboid
from pack_main.pack_sub import sphere

# User input 
length = float(input("Enter the length of the rectangle or cuboid: "))
width = float(input("Enter the width of the rectangle or cuboid: "))
height = float(input("Enter the height of the cuboid: "))
radius = float(input("Enter the radius of the circle or sphere: "))

# Rectangle
print("Area and perimeter of rectangle:")
print("Area:", length * width)
print("Perimeter:", 2 * (length + width))

# Circle 
print("Area and perimeter of circle:")
print("Area:", math.pi * radius ** 2)
print("Perimeter:", 2 * math.pi * radius)

# Cuboid 
print("Area and perimeter of cuboid:")
print("Surface Area:", 2 * (length * width + length * height + width * height))
print("Volume:", length * width * height)

# Sphere
print("Area and perimeter of sphere:")
print("Surface Area:", 4 * math.pi * radius ** 2)
print("Circumference:", 2 * math.pi * radius)
