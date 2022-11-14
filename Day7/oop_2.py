#inheritence
class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.li = [1, 2 ,3]
        
    def speak(self):
        print('Hi I am', self.name, 'I am ', self.age, 'years old')

    def talk(self):
        print('Bark')
    
class Cat(Dog):
    def __init__(self, name, age, color):
         super().__init__(name, age)
         self.color = color 
         self.name = 'tech'

    def talk(self):
        print('meow')

cat1 = Cat('micky', 3, 'white')
dog1 = Dog('tom', 3)

cat1.speak()
cat1.talk()

dog1.speak()
dog1.talk()

class Vechile():
    def __init__(self, price, color, gas):
        self.price = price
        self.gas = gas
        self.color = color

    def fillup(self):
        self.gas = 100

    def emptytank(self):
        self.gas = 0

    def gasleft(self):
        return self.gas

class Car(Vechile):
    def __init__(self, price, color, gas, speed):
        super().__init__(price, color, gas)
        self.speed =  speed
    def beep(self):
        print('BEEP BEEP')

class Truck(Car):
    def __init__(self, price, color, gas, speed,tires):
        super().__init__(price, color, gas, speed)
        self.tires = tires

    def beep(self):
        print('honk honk')

car1 = Car('2L', 'WHITE' , 'petrol', '15km')
car1.beep()

truck1 = Truck('5l', 'red', 'diesle', '15km', 8)
print(truck1.tires)
truck1.beep()