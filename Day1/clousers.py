#clousers

def outer_func():
    message = 'hi'
    def inner_func():
        print(message)
    return inner_func()
outer_func()




#assign variable to function
def outer_func():
    message = 'hi'
    def inner_func():
        print(message)
    return inner_func
my_func = outer_func()
my_func()
# print(my_func)

#passing parameter
def outer_func(msg):
    message = msg
    def inner_func():
        print(message)
    return inner_func
hii_func = outer_func('Hii')
hello_func = outer_func('Hello')
hii_func()
hello_func()

