class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. New Balance: {self.balance}")

    def display_balance(self):
        print(f"{self.name}'s Balance: {self.balance}")

# Test
acc = BankAccount("Rahul", 1000)
acc.display_balance()
acc.deposit(500)
acc.withdraw(200)

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book}")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Removed: {book}")
        else:
            print("Book not found")

    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Issued: {book}")
        else:
            print("Book not available")

    def return_book(self, book):
        self.books.append(book)
        print(f"Returned: {book}")

    def display_books(self):
        print("Available Books:", self.books)

lib = Library()
lib.add_book("Python Basics")
lib.add_book("OOPs in Python")
lib.display_books()

class Calculator:
    def add(self, a, b): return a + b
    def sub(self, a, b): return a - b
    def mul(self, a, b): return a * b
    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Division by zero not allowed"
        except Exception as e:
            return f"Error: {e}"

calc = Calculator()
print(calc.add(10, 5))
print(calc.div(10, 0))


