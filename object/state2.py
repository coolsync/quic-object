
# make single account
def make_account():
    account = {'balance': 0}
    return account

def despoit(account, amount):
    account['balance'] += amount
    return account['balance']

def withdraw(account, amount):
    account['balance'] -= amount
    return account['balance']

a = make_account()
b = make_account()

# print(despoit(b, 1000))
# print(withdraw(b, 10))

# class and objects
class BankAccount():
    def __init__(self):
        self.balance = 0
    
    def despoit(self,amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount

# Inheritance
class MinimumBankAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self) # balance = 0
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print('sorry, minimum balance must be maintained.')
        else:
            # self.balance -= amount
            BankAccount.withdraw(self, amount)

# a = BankAccount();
# b = BankAccount();

# c = MinimumBankAccount(200)
# c.balance = 1000
# print(c.minimum_balance)
# # c.minimum_balance = 200
# print(c.balance)
# c.withdraw(900)
# print(c.balance)

class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print(a.f(), b.f()) # A B
print(a.g(), b.g()) # A B



