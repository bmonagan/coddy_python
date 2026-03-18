from shape import Shape
from circle import Circle
from square import Square

# Test case handler
test_case = input()

if test_case == "base_shape":
    # Test the base Shape class
    shape = Shape("green")
    print(f"Color: {shape.color}")
    print(f"Area: {shape.area()}")
    print("Describe output:")
    shape.describe()

elif test_case == "circle_basics":
    # Test Circle creation and basic methods
    circle = Circle("red", 5)
    print(f"Color: {circle.color}")
    print(f"Radius: {circle.radius}")
    print(f"Area (rounded): {round(circle.area(), 2)}")
    print("Describe output:")
    circle.describe()

elif test_case == "square_basics":
    # Test Square creation and basic methods
    square = Square("blue", 4)
    print(f"Color: {square.color}")
    print(f"Side length: {square.side_length}")
    print(f"Area: {square.area()}")
    print("Describe output:")
    square.describe()

elif test_case == "various_sizes":
    # Test multiple instances with different dimensions
    shapes = [
        Circle("yellow", 2),
        Circle("orange", 7.5),
        Square("purple", 3),
        Square("black", 10)
    ]
    
    for i, shape in enumerate(shapes, 1):
        print(f"Shape {i}:")
        shape.describe()
        print(f"Area: {round(shape.area(), 2)}")
        print()  # Empty line for readability

elif test_case == "shape_polymorphism":
    # Test polymorphic behavior with a list of shapes
    shapes = [
        Shape("white"),
        Circle("red", 3),
        Square("blue", 4)
    ]
    
    print("Polymorphic behavior demonstration:")
    for shape in shapes:
        shape.describe()
        print(f"Area: {round(shape.area(shape_polymorphism), 2)}")
        print()  # Empty line for readability

elif test_case == "original_test_case":
    # Run the original test code from the challenge
    circle = Circle("red", 5)
    square = Square("blue", 4)

    # Test describe method
    circle.describe()
    square.describe()

    # Test area method
    print(f"Circle area: {circle.area()}")
    print(f"Square area: {square.area()}")