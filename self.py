class Car:
    def display_info(self):
        print(f"This car is a {self.year} {self.make} {self.model}")
    
from car import Car

# Test your code
my_car = Car()
my_car.year = 2020
my_car.make = "Toyota"
my_car.model = "Corolla"

my_car.display_info()  # Should print: This car is a 2020 Toyota Corolla