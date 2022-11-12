def add(x=12, y=4):
    return x*y

call = add()
print(call)


class Car(object):
    def __init__(self, make, model, year, condition='New', kms=10):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms

    def display(self, showAll):
        if showAll:
            return ('This car is a %s, %s from %s, it is %s and has %s.'%(self.make, self.model, self.year, self.condition, self.kms))
        else:
            return('This car is %s, %s from %s.' %(self.make, self.model, self.year))

car1 = Car('ford', 'fusion', 2012)
print(car1.display(True))

