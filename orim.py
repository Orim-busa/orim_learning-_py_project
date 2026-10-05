class BankAccount:
    def __init__(self, owner,  balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def witdraw(self, amount):
        if amount > self.balance:
            self.balance < amount
        else:
            print("insufficient funds")

# create account
Account1 = BankAccount("orim", 4000)
Account2 = BankAccount("busa", 8000)
Account3 = BankAccount("paul", 3000)

#run transaction
Account1.deposit(58000)
Account2.deposit(30000)
Account3.deposit(50000)

Account1.witdraw(300)
Account2.witdraw(3500)
Account3.witdraw(4600)

# print account detail and balance
print(Account1.owner, Account1.balance)
print(Account2.owner, Account2.balance)
print(Account3.owner, Account3.balance)

# make a list and add all the account 
Accounts = []

Accounts.append(Account1)
Accounts.append(Account2)
Accounts.append(Account3)

# loop through this 
for Account in Accounts:
    print(Account.owner, Account.balance)

owner = input("what is your name: ")
balance = int(input("how much do you want to deposit: "))
