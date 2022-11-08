def square_nums(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result
my_nums = square_nums([1,2,4,5,6])
print(my_nums)

#convert into generators
def square_nums(nums):
    for i in nums:
        yield(i*i)
my_nums= square_nums([1,2,3,4,5])
# print (next (my_nums) )
for num in my_nums:
    print(num)

#using list comprehensions
my_nums = [x*x for x in [1,2,3,4,5]]

my_nums = (x*x for x in [1,2,3,4,5]) #it prints generator object
print(list(my_nums))

#ex of generator
import memory_profiler as mem_profile
import random
import time

names = ['john','corey','sharf','cris','deo','thomas']
majors = ['math','engineering','compsci','arts', 'business','']

print ('Memor (Before): {}Mb'.format(mem_profile.memory_usage()))

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id':i,
            'names':random.choice(names),
            'majors':random.choice(majors)
            }
        result.append(person)
    return result

#generator
def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id':i,
            'names':random.choice(names),
            'majors':random.choice(majors)
            }
        yield (person)

# t1 = time.time
# people = people_list(1000000)
# t2 = time.time

t1 = time.time
people = people_generator(1000000)
t2 = time.time

print('Memory (After): {}Mb'.format(mem_profile.memory_usage()))
print('Took {} Seconds'.format(t2-t1))


