class Person:
    def __init__(self, name, age):
        # TODO: Initialize the Person class with name and age parameters
        # TODO: Store name and age as instance attributes (self.name, self.age)
        self.name = name
        self.age = age
    
    def introduce(self):
        # TODO: Implement the introduce method that prints a greeting
        # TODO: Print exactly: "Hi, I'm [name] and I'm [age] years old"
        # TODO: Use f-string formatting with self.name and self.age
        print(f"Hi, I'm {self.name} and I'm {self.age} years old")

# TODO: Import the Person class from person.py
from person import Person


class Employee(Person):
    def __init__(self, name, age, job):
        # TODO: Call the parent class constructor with name and age using super()
        # TODO: Store job as an instance attribute (self.job)
        super().__init__(name,age)
        self.job = job
    
    def introduce(self):
        # TODO: Override the introduce method to extend parent functionality
        # TODO: First call the parent's introduce method using super()
        # TODO: Then print exactly: "I work as a [job]" using self.job
        super().introduce()
        print(f"I work as a {self.job}")

# TODO: Import the Person class from person.py
# TODO: Import the Employee class from employee.py
from person import Person
from employee import Employee

def main():
    # TODO: Create a Person object with name "Alice" and age 30
    person = Person("Alice",30)
    
    # TODO: Create an Employee object with name "Bob", age 35, and job "Developer"
    employee = Employee("Bob", 35, "Developer")
    
    # TODO: Call the introduce() method on the Person object
    # Expected output: "Hi, I'm Alice and I'm 30 years old"
    person.introduce()
    # TODO: Print a blank line for spacing - print()
    print()
    # TODO: Call the introduce() method on the Employee object
    # Expected output: 
    # "Hi, I'm Bob and I'm 35 years old"
    # "I work as a Developer"
    employee.introduce()
if __name__ == "__main__":
    main()