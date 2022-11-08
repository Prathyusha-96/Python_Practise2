#class variables
class Employee:

    #creating class variable
    no_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

        Employee.no_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first , self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('john', 'deo', 50000)
emp_2 = Employee('test', 'user', 60000)

print(emp_1.email)
print(emp_1.fullname())
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
emp_1.raise_amount = 1.05
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
print(emp_1.__dict__)
print(Employee.no_of_emps)

#example
class Student:
    branch = 'ECE'

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

s1 = Student('john', 432)
s2 = Student('prathyusha', 427)
s1.branch = 'CSE'
print(s1.branch)
print(s2.branch)

print(Student.branch)
# print(s1.branch)
# print(s1.roll)

