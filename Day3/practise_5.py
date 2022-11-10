import array
for num in array.__dict__:
    print (num)

class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' +lname + '@gmail.com'

    def fullname(self):
        return ('{} {}'.format(self.fname, self.lname))

emp_1 = Employee('john', 'deo', 50000)

print(emp_1.email)
print(emp_1.fullname())

n = 10
i = 1
while i < n:
    if n%2 == 0:
        print('even no')
    else:
        print('odd no')
    i += 1

class Bankaccount:
    def __init__(self, balance):
        self.balance = balance
        

    def bal_withdraw(self, amount):
        self.balance -= amount
        return (self.balance)

    def bal_deposite(self, amount):
        self.balance += amount
        return (self.balance)


a = Bankaccount(5000)
b = Bankaccount(7000)


print(a.bal_withdraw(1000))
print(b.bal_deposite(10000))