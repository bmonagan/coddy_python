class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def display_info(self):
        # TODO: Implement a display_info method that prints vehicle information
        # TODO: Print in format: "Vehicle: [make] [model]"
        # TODO: Use f-string formatting: f"Vehicle: {self.make} {self.model}"
        print(f"Vehicle: {self.make} {self.model}")
# TODO: Import the Vehicle class from vehicle.py
# Use format: from vehicle import Vehicle
from vehicle import Vehicle
class Car(Vehicle):
    pass
    
from car import Car
from vehicle import Vehicle

# TODO: Create a Vehicle object with make "Toyota" and model "Corolla"
vehicle = Vehicle("Toyota", "Corolla")

# TODO: Create a Car object with make "Honda" and model "Civic"
car = Car("Honda", "Civic")

# TODO: Call display_info() method on the vehicle object
# Expected output: "Vehicle: Toyota Corolla"
vehicle.display_info()
# TODO: Call display_info() method on the car object
# Expected output: "Vehicle: Honda Civic"
car.display_info()
# Note: Car inherits display_info from Vehicle without modification