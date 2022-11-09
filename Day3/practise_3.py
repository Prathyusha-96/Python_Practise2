#classes
class Myclass:
    x = 2

a = Myclass()
print(a.x)

class Vechile:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vechile):
    def __init__(self,max_speed, mileage, busname):
        super().__init__(max_speed, mileage)
        self.busname = busname
    def vechile_name(self):
       return('Vechile name: school {} : speed : {}, milege: {}'.format(self.busname,self.max_speed, self.mileage))


model = Bus(250, 80 , 'volvo')
print(model.vechile_name())

class Vechile:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vechile):
    pass

school_bus = Bus('school volvo', 180, 12)
print('Vechile name:', school_bus.name, 'speed:', school_bus.max_speed, 'milege:', school_bus.mileage)

#Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.
class Vechile:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vechile):
    def __init__(self, name, max_speed, mileage, capacity):
         super().__init__(name,max_speed, mileage)
         self.capacity = capacity

    def seating_capacity(self):
        return('The seating capacity of a {} is {} passangers'.format(self.name, self.capacity))

bus = Bus('volvo', 180, 12, 50)
print(bus.seating_capacity())

#define property
class Vehicle:
    color = 'white'

    def __init__(self,  name, max_speed, mileage):
        
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

vechile_1 = Bus('school volvo', 180, 12)
vechile_2 = Car('Audi q5', 200, 18)

print(vechile_1.color, vechile_1.name, "Speed:", vechile_1.max_speed, "Mileage:", vechile_1.mileage)
print(vechile_2.color, vechile_2.name, "Speed:", vechile_2.max_speed, "Mileage:", vechile_2.mileage)

