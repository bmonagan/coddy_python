class Device:
    # TODO: Implement the power_on method
    # TODO: This method should return the string "Device powered on"
    def power_on(self):
        return "Device powered on"
# TODO: Import the Device class from device.py
from device import Device

class Computer(Device):
    # TODO: Override the power_on method from the Device class
    # TODO: This method should return the string "Computer powered on"
    def power_on(self):
        return "Computer powered on"
# TODO: Import the Screen class from screen.py
# TODO: Import the Computer class from computer.py
from screen import Screen
from computer import Computer

class Laptop(Screen, Computer):
    # TODO: Notice that Laptop inherits from both Screen and Computer
    # TODO: The order of inheritance is important (Screen first, then Computer)
    # TODO: No need to override power_on() - it will use the MRO to determine which method to call
    pass
from device import Device
from screen import Screen
from computer import Computer
from laptop import Laptop

def explain_mro(class_name):
    print(f"MRO for {class_name.__name__}:")
    for cls in class_name.__mro__:
        print(cls.__name__)
    
    instance = class_name()
    result = instance.power_on()
    print(f"Power on result: {result}")
    print()  # Empty line for better readability
    
# Test your code
explain_mro(Device)
explain_mro(Screen)
explain_mro(Computer)
explain_mro(Laptop)
# TODO: Import the Device class from device.py
from device import Device

class Screen(Device):
    # TODO: Override the power_on method from the Device class
    # TODO: This method should return the string "Screen powered on"
    def power_on(self):
        return "Screen powered on"