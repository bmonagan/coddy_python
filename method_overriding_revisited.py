# TODO: Import the Vehicle class from vehicle.py
from vehicle import Vehicle

class Truck(Vehicle):
    # TODO: No need to implement __init__ as it will use the parent class constructor
    
    # TODO: Override the start() method to return "Truck diesel engine started"
    def start(self):
        return "Truck diesel engine started"
    
    # TODO: Override the fuel_efficiency() method to return 15
    def fuel_efficiency(self):
        return 15
from vehicle import Vehicle
from car import Car
from motorcycle import Motorcycle
from truck import Truck

def vehicle_info(vehicle):
    return f"{vehicle.make} {vehicle.model}: {vehicle.start()}, Efficiency: {vehicle.fuel_efficiency()} mpg"


# Test with different vehicles - DO NOT MODIFY THIS TEST CODE
vehicles = [
    Car("Toyota", "Camry"),
    Motorcycle("Harley", "Davidson"),
    Truck("Ford", "F-150"),
    Vehicle("Generic", "Vehicle")
]

for v in vehicles:
    print(vehicle_info(v))
class Vehicle:
    # TODO: Initialize the Vehicle class with make and model parameters
    # TODO: Store make and model as instance attributes (self.make, self.model)
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    # TODO: Implement the start() method that returns "Vehicle started"
    def start(self):
        return "Vehicle started"
    
    # TODO: Implement the fuel_efficiency() method that returns 0
    def fuel_efficiency(self):
        return 0