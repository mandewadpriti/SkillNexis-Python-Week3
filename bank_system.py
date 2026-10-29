# Bank Account System
class Account:
    def __init__(self, acc_no, holder, balance=0):
        self.acc_no=acc_no; self.holder=holder; self.balance=balance
    def deposit(self, amount):
        self.balance+=amount; print(f"Deposited {amount}, Balance: {self.balance}")
    def withdraw(self, amount):
        if amount<=self.balance:
            self.balance-=amount; print(f"Withdrew {amount}, Balance: {self.balance}")
        else: print("Insufficient Balance!")
    def display(self):
        print(f"Acc No: {self.acc_no}, Holder: {self.holder}, Balance: {self.balance}")

class SavingsAccount(Account):
    def add_interest(self, rate=0.05):
        interest=self.balance*rate
        self.balance+=interest
        print(f"Interest Added: {interest}, New Balance: {self.balance}")

acc=SavingsAccount(101,"Priti",5000)
acc.display(); acc.deposit(2000); acc.withdraw(1000); acc.add_interest()
