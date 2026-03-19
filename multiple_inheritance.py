class Device:
    def __init__(self, brand):
        self.brand = brand
    
    def power_on(self):
        # TODO: Return the string "Device powered on"
        return "Device powered on"
class Internet:
    def connect(self):
        # TODO: Return the string "Connected to the internet"
        return "Connected to the internet"
# TODO: Import the Device class from device.py
# TODO: Import the Internet class from internet.py
from device import Device
from internet import Internet

class Smartphone(Device, Internet):
    def __init__(self, brand, model):
        # TODO: Call the parent class (Device) constructor with the brand parameter using super()
        # TODO: Store the model parameter as an instance attribute (self.model)
        super().__init__(brand)
        self.model = model
    
    def make_call(self, number):
        # TODO: Return a formatted string "Calling {number}" where {number} is the parameter value
        return (f"Calling {number}")
# TODO: Import the Smartphone class from smartphone.py
from smartphone import Smartphone

# Create a smartphone and test its methods
# TODO: Create a Smartphone object with brand "Apple" and model "iPhone 13"
my_phone = Smartphone("Apple","iPhone 13")

# TODO: Call and print the power_on() method of the smartphone
print(my_phone.power_on())

# TODO: Call and print the connect() method of the smartphone
print(my_phone.connect())
# TODO: Call and print the make_call() method of the smartphone with parameter "123-456-7890"
print(my_phone.make_call("123-456-7890"))