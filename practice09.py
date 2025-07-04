def deposit(balance,amount):
    if amount>0:
        balance+=amount
def withdraw(balance,amount):
    if amount<=balance:
        balance-=amount
def check_balance(balance):
    print(f"Check balance: {balance}")
balance=100
balance=deposit(balance=balance,amount=20)
check_balance(balance)
