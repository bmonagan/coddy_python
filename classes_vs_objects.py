# Import the Student class
from student import Student

# TODO: Create two student objects
student1 = Student()
student2 = Student()


# TODO: Add attributes to student1
student1.name = "Alice"
student1.grade = "A"
# TODO: Add attributes to student2
student2.name = "Bob"
student2.grade = "B"

# Print student information
print(f"{student1.name} has grade {student1.grade} at {Student.school}")
print(f"{student2.name} has grade {student2.grade} at {Student.school}")