class Temperature:
    def __init__(self, celsius):
        # Store the temperature, but use the setter for validation
        self.celsius = celsius
    
    # TODO: Create a property decorator for celsius that returns self._celsius
    @property
    def celsius(self):
        return self._celsius
    
    # TODO: Create a celsius.setter that validates the temperature is above absolute zero (-273.15°C)
    # TODO: If value < -273.15, raise ValueError with message "Temperature cannot be below absolute zero (-273.15°C)"
    # TODO: Otherwise, set self._celsius to the value
    @celsius.setter
    def celsius(self,temperature):
        if temperature < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
        else:
            self._celsius = temperature
    
    # TODO: Create a property decorator for fahrenheit that converts Celsius to Fahrenheit
    # TODO: Use the formula: F = C × 9/5 + 32
    @property
    def fahrenheit(self):
        return self.celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9

# TODO: Import the Temperature class from the temperature module
from temperature import Temperature

# Test the class:
# TODO: Create a temperature instance at 25°C
temp = Temperature(25)

# TODO: Print both Celsius and Fahrenheit values
# TODO: Use the format: "25.0°C is 77.0°F"
print(f"{temp.celsius}°C is {temp.fahrenheit}°F")

# TODO: Set the temperature to 98.6°F
temp.fahrenheit = 98.6

# TODO: Print both values again to confirm the conversion works
# TODO: Use the same format as before
print(f"{temp.celsius}°C is {temp.fahrenheit}°F")