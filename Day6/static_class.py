class Person:
    population = 50
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def getpopulation(cls, incr):
        cls.population = incr
        return incr

    @staticmethod
    def isadult(age):
        return age >= 18

    def display(self):
        return('{} is {} years old'.format(new_person.name, new_person.age))


new_person = Person('john', 20)

print(Person.getpopulation(100))
print(new_person.display())
print(new_person.isadult(22))