class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last  = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return ('{} {}'.format(self.first, self.last))

    def apply_raise(self):
            self.pay = int(self.pay * self.raise_amount)

#creating subclass
class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, first, last, pay, prog_lng):
        super().__init__(first, last, pay)
        self.prog_lng = prog_lng

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('---->', emp.fullname())

# dev_1 = Employee('john', 'deo', 50000)
# dev_2 = Employee('test', 'cris', 60000)

dev_1 = Developer('john', 'deo', 50000, 'python')
dev_2 = Developer('test', 'cris', 60000, 'javascript')

mgr_1 = Manager('jack', 'smith', 90000, [dev_1])

# print(mgr_1.email)
# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)

# mgr_1.print_emps()
# print(dev_1.email)
# print(dev_1.prog_lng)

print(isinstance(mgr_1, Manager))

print(issubclass(Manager, Manager))

#METHOD resolution order
# print(help(Developer))

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

