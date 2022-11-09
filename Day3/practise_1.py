#generators

def my_gen():
    n = 1
    print('this is first statement')
    yield (n)
    
    n += 1
    print('this is second statement')
    yield (n)
    
    n += 1
    print('this is third statement')
    yield (n)

for i in my_gen():
    print(i)

#reverse a string

def rev_str(my_str):
    length = len(my_str)
    for i in range(length -1, -1, -1):
        yield my_str[i]

for char in rev_str('hello'):
    print(char)


#using list comprehension

my_list = [1,2,3,5,6]
list1 = [x**2 for x in my_list]
print(list1)

#using generator

result = list(x**2 for x in my_list)
print(result)

#fibonacci sequence
def fib(limit):
    a,b = 0,1
    while a < limit:
        yield a
        a, b = b, a+b

x = fib(5)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

#for loop
for i in fib(6):
    print(i)

# A Simple Python program to demonstrate working
# of yield

# A generator function that yields 1 for the first time,
# 2 second time and 3 third time


def simpleGeneratorFun():
    
	yield 1
	yield 2
	yield 3

# Driver code to check above generator function
for value in simpleGeneratorFun():
	print(value)




