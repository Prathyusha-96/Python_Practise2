#how can you randomize the items of a list in place in Python?
import random
from random import shuffle
x = ['red', 'green', 'white', 'yellow', 'blue']
shuffle(x)
print(x)

#What is the difference between Python Arrays and lists?
import array as arr
my_array = arr.array('i', [1, 2, 3])
my_list = [1, 2, 3]
print(my_array)
print(my_list)

#What are functions in Python?
#Ans: A function is a block of code which is executed only when it is called. 
# To define a Python function, the def keyword is used.

def func():
   print('hello world')
func()

#lambda function
a = lambda x,y : x+y
print(a(5,6))