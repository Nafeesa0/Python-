class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.breadth = w

    def rectangle_area(self):
        return self.length * self.breadth

    def rectangle_peri(self):
        return 2 * (self.length + self.breadth)


# Input for the first rectangle
length1 = float(input("Enter the length of the first rectangle: "))
breadth1 = float(input("Enter the breadth of the first rectangle: "))
rectangle1 = Rectangle(length1, breadth1)

# Input for the second rectangle
length2 = float(input("Enter the length of the second rectangle: "))
breadth2 = float(input("Enter the breadth of the second rectangle: "))
rectangle2 = Rectangle(length2, breadth2)

# Calculations and outputs
print("Area of Rectangle 1 =", rectangle1.rectangle_area())
print("Area of Rectangle 2 =", rectangle2.rectangle_area())
print("Perimeter of Rectangle 1 =", rectangle1.rectangle_peri())
print("Perimeter of Rectangle 2 =", rectangle2.rectangle_peri())

# Comparing areas
if rectangle1.rectangle_area() == rectangle2.rectangle_area():
    print("Areas are Equal")
else:
    print("Areas are not Equal")
