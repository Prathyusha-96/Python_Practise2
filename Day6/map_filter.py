li = [1, 2, 4, 5, 6]
new_list = []
for i in li:
    new_list.append(i**i)
print(new_list)

li1 = [2, 5, 8, 6]
new_li = []
def square_nums(num):
    return num**num

for num in li1:
    new_li.append(square_nums(num))
print(new_li)

print(4**4)

li2 = [1, 2, 3, 4, 5]
def func(x):
    return x**x
print(list(map(func, li2)))

a = [1,2,3,4]
def add5(x):
    return x+5
print(list(map(add5, a)))

#lambda functions with map
tup = (1,2,3,4,5,6)
result = tuple(map(lambda x: x *2, tup))
print(result)


#filter
def add(x):
    return x+7

def isodd(x):
    return x%2 != 0

a = [1,2,3,5,4,6]
print(list(filter(isodd, a)))

def func(x):
    if x>=3:
        return x
y = filter(func, (1,2,3,4))
print(list(y))

#lambda filter

tup = (1,2,3,4,5,6)
result = (filter(lambda x: (x>=3), tup))
print(list(result))