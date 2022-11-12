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

#filter
def add(x):
    return x+7

def isodd(x):
    return x%2 != 0

a = [1,2,3,5,4,6]
print(list(filter(isodd, a)))