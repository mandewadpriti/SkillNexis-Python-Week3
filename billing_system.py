# Mini Project W3: Billing System
class Product:
    def __init__(self, name, price, quantity):
        self.name=name; self.price=price; self.quantity=quantity
    def total_price(self):
        return self.price*self.quantity

class Bill:
    def __init__(self, tax_rate=0.18):
        self.products=[]
        self.tax_rate=tax_rate
    def add_product(self, product):
        self.products.append(product)
    def display_bill(self):
        print("-"*55)
        for p in self.products:
            print(f"{p.name} - {p.price} x {p.quantity} = {p.total_price()}")
        print("-"*55)
        subtotal=sum(p.total_price() for p in self.products)
        tax=subtotal*self.tax_rate
        print(f"Subtotal: {subtotal}")
        print(f"Tax: {tax:.2f}")
        print(f"Grand Total: {subtotal+tax:.2f}")

bill=Bill()
bill.add_product(Product("Laptop",50000,1))
bill.add_product(Product("Mouse",500,2))
bill.add_product(Product("Keyboard",1500,1))
bill.display_bill()
