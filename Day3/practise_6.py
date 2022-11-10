class Dog:
    def __init__(self,name):
        self.name = name
        
Rodger = Dog('puppy')
Tommy = Dog('cutie')
print(Rodger.name)

#<!---!>

class Person:
    
    bonus_amt = 1.05

    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay
        
    @property
    def details(self):
        return ('My name is {}, Iam {} years old'.format(self.name, self.age))

    def get_bonus(self):
        self.pay = int(self.pay * self.bonus_amt)

    @classmethod
    def get_raise(cls,amount):
        cls.bonus_amt = amount

p1 = Person('john', 25, 25000)
p2 = Person('deo', 26,  40000)

# p1.bonus_amt = 1.06
# print(p2.details)
Person.get_raise(1.06)
print(Person.bonus_amt)
print(p1.bonus_amt)
p1.get_raise(1.06)
print(p1.pay)
# p1.get_bonus()
# print(p1.pay)

