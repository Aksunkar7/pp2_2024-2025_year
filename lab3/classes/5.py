class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, money):
        if self.balance - money < 0:
            print("Not enough money!")
        else:
            self.balance -= money
            
            print(f"Your balance now: {self.balance}")
            print(self.owner + "'s profit will:", money*0.14, "in 1 year")
        
    def withdraw(self, money):
        if self.balance - money < 0:
            print("Not enough money!")
        else:
            self.balance -= money
            print(f"Your balance now: {self.balance}")
            
a = Account(input("Name:"), int(input("Balance:")))

a.deposit(int(input("How much deposit:")))
a.withdraw(int(input("How much you want withdraw:")))