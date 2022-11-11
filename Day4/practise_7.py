class Person:
    def __init__(self, name, idnumber):
      self.name = name
      self.idnumber = idnumber

    def details(self):
        return 'My name is {}'.format(self.name)

    def __repr__(self):
        return 'Employee {}, {}, {}'.format(self.name, self.idnumber, self.post)

    def __str__(self):
        return '{} '.format(self.display())

class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        super().__init__(name, idnumber)
        self.salary = salary
        self.post = post

    def display(self):
        return 'id number: {}, post: {}'.format(p1.idnumber, p1.post)

p1 = Employee('Johny', 123456, 50000, 'Developer')

# print(isinstance(p1, Employee))
# print(issubclass(Employee, Person))

# print(repr(p1))
# print(str(p1))

print(p1.__repr__())
print(p1.__str__())
print(len(p1.post))