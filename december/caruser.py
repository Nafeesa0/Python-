class Cars: 
    def cars(self):
        print("Car Details:", self.company, self.price, self.colour)

# Function to get car details from user
def get_car_details():
    company = input("Enter the company name: ")
    price = float(input("Enter the price of the car: "))
    colour = input("Enter the color of the car: ")
    return company, price, colour

# Create car objects and get details from user
car1 = Cars()
car1.company, car1.price, car1.colour = get_car_details()

car2 = Cars()
car2.company, car2.price, car2.colour = get_car_details()

car3 = Cars()
car3.company, car3.price, car3.colour = get_car_details()

# Display car details
car1.cars()
car2.cars()
car3.cars()
