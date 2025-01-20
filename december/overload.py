class Rectangle:
    def __init__(self):
        self.__length = 1.0
        self.__width = 1.0

    def __str__(self):
        return "This is class Rectangle"

    def set_length(self, len=1.0):  # Default value len=1.0
        self.__length = len

    def set_width(self, wid=1.0):  # Default value wid=1.0
        self.__width = wid

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_area(self):
        return self.get_width() * self.get_length()

    def __lt__(self, other):
        if self.get_area() < other.get_area():
            return "1st Rectangle is Smaller."
        else:
            return "2nd Rectangle is Smaller."


# Create first rectangle instance with user input
my_rect1 = Rectangle()
length1 = float(input("Enter the length of the first rectangle: "))
width1 = float(input("Enter the width of the first rectangle: "))
my_rect1.set_length(length1)
my_rect1.set_width(width1)
print("The length is ", my_rect1.get_length())
print("The width is  ", my_rect1.get_width())
print("The area is   ", my_rect1.get_area())
print(my_rect1)

# Create second rectangle instance with user input
my_rect2 = Rectangle()
length2 = float(input("Enter the length of the second rectangle: "))
width2 = float(input("Enter the width of the second rectangle: "))
my_rect2.set_length(length2)
my_rect2.set_width(width2)
print("The length is ", my_rect2.get_length())
print("The width is  ", my_rect2.get_width())
print("The area is   ", my_rect2.get_area())
print(my_rect2)

# Compare areas of the two rectangles
print(my_rect1 < my_rect2)
