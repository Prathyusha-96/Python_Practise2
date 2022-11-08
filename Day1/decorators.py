#first calss functions
def outer_func():
    message = 'Hi'
    def inner_func():
        print(message)
    return inner_func()
outer_func()

#clousers
def outer_func():
    message = 'Hi'
    def inner_func():
        print(message)
    return inner_func
my_func = outer_func()
my_func()
# print(my_func)

#passing arguments
def outer_func(msg):
    def inner_func():
        print(msg)
    return inner_func


hi_func = outer_func('hi')
bye_func = outer_func('bye')

hi_func()
bye_func()

#Decorators
#it is a function that takes another function as an argument

def decorator_func(message):
    def wrapper_func():
        print(message)
    return wrapper_func

def decorator_func(original_func):
    def wrapper_func(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_func.__name__))
        return original_func(*args, **kwargs)

    return wrapper_func

#using decorator func
@decorator_func
def display():
    print('display function ran')
# decorated_display = decorator_func(display)
# decorated_display()
# display()
@decorator_func
def display_info(name,age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('john', 26)

display()

#class method
class decorator_class:
    def __init__(self, original_func):
        self.original_func = original_func

    def __call__ (self, *args, **kwargs):
        print('call method executed this before {}'.format(self.original_func.__name__))
        return self.original_func(*args, **kwargs)

@decorator_class
def display():
    print('display function ran')

@decorator_class
def display_info(name,age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('john', 26)

display()

        

