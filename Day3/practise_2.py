#treating the functions as objects
def my_func(text):
    return text.upper()
# print(my_func('hello'))

#creating object
result = my_func('hello')
print(result)

#passing the function as an arugument

def name_1(text):
    return text.upper()

def name_2(text):
    return text.lower()

def greet(func):
    #creating variable
    greeting = func('My Name Is Prathyusha')
    print(greeting)

greet(name_1)
greet(name_2)

#function can return another function
def create_add(x):
    def adder(y):
        return x+y
    return adder(10)

add_15 = create_add(15)
print(add_15)

#decorator
def decorator_func(original_func):
    def wrapper_func(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_func.__name__))
        return original_func(*args, **kwargs)

    return wrapper_func
@decorator_func
def display():
    print('display function ran')
display()


def hello_decorator(func):
    def inner1():
        print('hello this is before function execution')
        func()
        print('this is after function execution')
    return inner1

@hello_decorator
def function_to_be_used():
    print('this is inside function')

# function_to_be_used = hello_decorator(function_to_be_used)

function_to_be_used()

#normal function
def my_func(name):
    # return name
    print(name)
my_func('prathyusha')

#example
def smart_divide(func):
    def divide_inner(a, b):
        print('iam going to divide', a ,'and', b)
        if b == 0:
            print('cannot divide')
            return
        return func(a, b)
    return divide_inner

@smart_divide
def divide_outer(a,b):
    print(a/b)

divide_outer(10,0)
