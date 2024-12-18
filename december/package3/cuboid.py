# Get length, width, and height
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
height = float(input("Enter the height: "))

# Calculate and display surface area and volume
print("Area and perimeter of cuboid is:")
print("Surface Area:", 2 * (length * width + length * height + width * height))
print("Volume:", length * width * height)
