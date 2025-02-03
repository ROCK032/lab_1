class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}, New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}, New balance: {self.balance}")
        else:
            print("Error")

account = Account("Alice", 1000)

account.deposit(500)
account.deposit(200)

account.withdraw(300)
account.withdraw(2000)
