class BankAccount:
    # TODO: Add class attribute here
    bank_name = "Python National Bank"
    
    # TODO: Add the methods here
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def get_balance(self):
        print(f"Current balance: ${self.balance}")
===================
from bank_account import BankAccount

# Create an account and test your methods
my_account = BankAccount()
my_account.balance = 0  # Starting balance

my_account.deposit(100)
my_account.withdraw(30)
my_account.get_balance()