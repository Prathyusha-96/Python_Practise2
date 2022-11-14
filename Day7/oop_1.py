#class
x = 5
y = 'hello'
print(type(x))
print(type(y))
# help(int)
# help(str)

class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.li = [1, 2 ,3]
        
    def speak(self):
        print('Hi I am', self.name, 'I am ', self.age, 'years old')
    
    def change_age(self, age):
        self.age = age
    
    def add_weight(self, weight):
        self.weight = weight

dog1 = Dog('Puppy', 3)
dog2 = Dog('Tom', 5)

# print(dog1.name)
# print(dog2.name)
dog1.change_age(5)
dog1.speak()
dog2.speak()
print(dog1.li)
dog1.add_weight(50)
print(dog1.weight)
dog2.add_weight(70)
print(dog2.weight)

