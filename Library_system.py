# Library System
class Book:
    def __init__(self, title, author, available=True):
        self.title=title; self.author=author; self.available=available
class Library:
    def __init__(self):
        self.books=[]
    def add_book(self, book):
        self.books.append(book)
    def display_books(self):
        for b in self.books:
            status="Available" if b.available else "Issued"
            print(f"{b.title} by {b.author} - {status}")
    def borrow_book(self, title):
        for b in self.books:
            if b.title==title and b.available:
                b.available=False; print(f"Borrowed {title}"); return
        print("Not Available")

lib=Library()
lib.add_book(Book("Python Basics","John"))
lib.add_book(Book("OOP Concepts","Smith"))
lib.display_books()
lib.borrow_book("Python Basics")
lib.display_books()
