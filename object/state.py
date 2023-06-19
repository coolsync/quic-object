balance = 0

# drop global: UnboundLocalError: local variable 'balance' referenced before assignment
def deposit(amount):
    global balance
    balance += amount
    return balance

def withdraw(amount):
    global balance
    balance -= amount
    return balance

deposit(1000)
print(balance)
withdraw(100)
print(balance)
