class Cars:
    def cars(self):
        print("Car Details:", self.company, self.price, self.colour)


car1 = Cars()
car1.company = "Toyota"
car1.price = 900000 
car1.colour = "Red"

car2 = Cars()
car2.company = "Honda"
car2.price = 340000
car2.colour = "Blue"

car3 = Cars()
car3.company = "Suzuki"
car3.price = 500000
car3.colour = "Black"


car1.cars()
car2.cars()
car3.cars()
