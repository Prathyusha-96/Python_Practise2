import collections
from collections import Counter

c = Counter('galad')
print(c)
c = Counter(['a', 'b', 'c', 'b', 'a'])
print(c)
e = Counter({'a':1, 'b':2})
print(c)
d= Counter(cats=4, dogs=7)
print(c)
print(list(c.elements()))

c = Counter(a=4, b=2, c=0, d=-2)
d= ['a','b', 'b', 'c']
c.subtract(d)
print(c)
c.update(d)
print(c)
c.clear()
print(c)

c = Counter(a=4, b=2, c=0, d=-2)
d= Counter(['a','b', 'b', 'c'])
print(c+d)
print(c-d)
print(c&d) #intersection
print(c|d) #union

#named tuple

from collections import namedtuple
colors = namedtuple('Color', ['red', 'blue', 'green'])
white = colors(55, 125, 125)

print(white.red)

Student = namedtuple('Student', ['name', 'age', 'id'])
student = Student('John', 25, '1234556')

#access through index
print(student[0])

#access through name key
print(student.name)

#example

Point = namedtuple('Point', ['x','y', 'z'])
newp = Point(2, 3, 5)
print(newp)
print(newp._fields)

newp = newp._replace(x=5)
print(newp)

p2 = Point._make(['a', 'b', 'c'])
print(p2)
#collections deque
from collections import deque
d = deque('hello')
print(d)
d.append('4')
d.appendleft('5')
print(d)
d.pop()
print(d)
d.popleft()
print(d)
d.clear()
print(d)
d.extend('456')
print(d)
d.extend('hello')
print(d)
d.extend([1, 2, 3])
print(d)
d = deque('hello', maxlen=5)
print(d)
d.append(1)
print(d)

