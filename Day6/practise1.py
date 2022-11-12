#generators 
def squarenum(num):
    yield num * num
for i in squarenum(5):
    print (i)

def outer_func():
    message = 'Hi'
    def inner_func():
        print(message)
    return inner_func
my_func = outer_func()
my_func()