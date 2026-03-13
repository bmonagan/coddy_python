class Book:
    # TODO: Add the __init__ method that takes title, author, and pages parameters
    # TODO: Initialize the title, author, and pages attributes using self
    # Example: self.title = title
     
     def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages


# TODO: Import the Book class from book.py
# Use this format: from book import Book
from book import Book
# TODO: Create a book object named 'my_book' with the following values:
# - title: "Harry Potter"
# - author: "J.K. Rowling"
# - pages: 400
# Example: my_book = Book("Title", "Author", pages)
my_book = Book("Harry Potter", "J.K. Rowling", 400)

# Print book details
# TODO: Make sure my_book is properly defined before this line runs
print(f"'{my_book.title}' by {my_book.author}, {my_book.pages} pages")
    