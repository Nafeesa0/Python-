import math

# Get radius
radius = float(input("Enter the radius: "))

# Calculate and display surface area and circumference
print("Area and perimeter of sphere:")
print("Surface Area:", 4 * math.pi * radius ** 2)
print("Circumference:", 2 * math.pi * radius)


# pack_sub/sphere.py
import math

def area(radius):
    return 4 * math.pi * radius ** 2

def volume(radius):
    return (4/3) * math.pi * radius ** 3
