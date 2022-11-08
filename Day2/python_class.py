#create a class
class MyClass:
    x = 2
#create object
p1 = MyClass()
print(p1.x)

#basic class create
class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first = 'john'
emp_1.last = 'deo'
emp_1.email = 'john.deo@gmail.com'
emp_1.pay = 50000

emp_2.first = 'cris'
emp_2.last = 'leo'
emp_2.email = 'cris.leo@gmail.com'
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)

#__init__ function

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

p1 = Person('john', 25)
print(p1.age)

#example
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@gmail.com'

    #using function
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('john', 'deo', 50000)
emp_2 = Employee('cris', 'leo', 60000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())

#get full name
# print('{} {}'.format(emp_1.first, emp_1.last))