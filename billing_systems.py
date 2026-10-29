class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

class Bill:
    def __init__(self, tax_rate=0.18):
        self.products = []
        self.tax_rate = tax_rate

    def add_product(self, product):
        self.products.append(product)

    def calculate_bill(self):
        subtotal = sum(p.total_price() for p in self.products)
        tax = subtotal * self.tax_rate
        total = subtotal + tax
        return subtotal, tax, total

    def display_bill(self):
        print("-" * 50)
        print(f"{'Product':<15} {'Price':<10} {'Qty':<5} {'Total':<10}")
        print("-" * 50)
        for p in self.products:
            print(f"{p.name:<15} {p.price:<10} {p.quantity:<5} {p.total_price():<10}")
        print("-" * 50)
        subtotal, tax, total = self.calculate_bill()
        print(f"Subtotal: {subtotal}")
        print(f"Tax ({self.tax_rate*100}%): {tax:.2f}")
        print(f"Grand Total: {total:.2f}")
        print("-" * 50)

# Demo
bill = Bill()
bill.add_product(Product("Laptop", 50000, 1))
bill.add_product(Product("Mouse", 500, 2))
bill.add_product(Product("Keyboard", 1500, 1))
bill.display_bill()