#STR( ) repr()

s = 'Hello World'
print(str(s))
print(str(2.0/11.5))

print(repr(s))
print(repr(2.0/11.5))

import datetime
today = datetime.datetime.now()
print(str(today))
print(repr(today))

class FlashCard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
       return(self.word+'('+self.meaning+')')


result = FlashCard('DSA', 'Dtatstructures and algorithms')
flash = []
flash.append(result)
for i in flash:
    print(i)
print(flash)
# while(True):
#     word = "DSA"
#     meaning = "Datastructures an Algorithms"
#     flash.append(FlashCard(word, meaning))

#     for i in flash:
#         print('>', i)

#How to count number of instances of a class in Python?

class Dog:
    counter = 0
    def __init__(self):
        Dog.counter += 1

s1 = Dog()
s2 = Dog()
s3 = Dog()

print(Dog.counter)

def add(x):
    return x+7

def isodd(x):
    return x%2 != 0

a = (1,2,3,5,4,6)
print(tuple(filter(isodd, a)))

def func(x):
    if x>=3:
        return x
y = filter(func, (1,2,3,4))
print(list(y))

