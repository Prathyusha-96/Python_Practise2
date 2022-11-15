import mod
from mod import NotPrivate
test = NotPrivate('tim')
test.display()
test.__display()

#overriding methods
class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y


    def __add__(self, other1):
        return (self.x + other1.x, self.y + other1.y)

    def __str__(self):
        return f'{self.x} and {self.y}'

p1 = Point(3, 4)
p2 = Point(3, 2)
p3 = Point(2, 4)
p4 = Point(0, 1)
p5 = p1 + p2
print(p5)


print(p4)