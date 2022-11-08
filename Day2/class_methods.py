#class methods and static methods

class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return ('{} {}'.format(self.first, self.last))

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    #using classmethod
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

emp_1 = Employee('John', 'Deo', 50000)
emp_2 = Employee('Cris', 'Leo', 60000)

# Employee.set_raise_amount(1.05)
emp_1.set_raise_amount(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_1.email)
print(emp_1.fullname())
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

#using classmethod

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    @classmethod
    def from_str(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
#example
emp_str_1 = 'john-deo-70000'
emp_str_2 = 'test-user-60000'
emp_str_3 = 'cris-leo-50000'

# first, last, pay = emp_str_1.split('-')

# new_emp_1 = Employee(first, last, pay)
new_emp_1 = Employee.from_str(emp_str_2)
print(new_emp_1.email)
print(new_emp_1.pay)

#static method
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('John', 'Deo', 50000)
emp_2 = Employee('Cris', 'Leo', 60000)

import datetime
my_date = datetime.date(2022, 11, 5)
print(Employee.is_workday(my_date))


