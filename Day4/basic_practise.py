#Reverse each word of a string
#str = 'My Name is Jessa'

def reverse_words(sentence):
    words = sentence.split(' ')
    new_word_list = [word[::-1] for word in words]

    reverse_str = " ".join(new_word_list)
    return reverse_str

str1 = "My Name is Jessa"
print(reverse_words(str1))

#Read text file into a variable and replace all newlines with space

with open('sample.txt', 'r') as file:
    data = file.read().replace('\n', ' ')
    print(data)

#Remove items from a list while iterating
number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
i = 1
n = len(number_list)
while i < n:
    if number_list[i] > 50:
        del number_list[i]
        n = n-1
    else:
        i += 1

print(number_list)
       
#Display all duplicate items from a list

sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]

exist = {}
duplicates = []
for x in sample_list:
    if x not in exist:
        exist[x] = 1
    else:
        duplicates.append(x)

print(duplicates)

#create an inner function
def outer_func(x, y):
    def inner_func(x,y):
       return x + y
    z = inner_func(x,y)
    return z + 'Developers'
result = outer_func('Emma','kelly')
print(result)


list1 = [5, [10, 15, [20, 25, [30, 35], 40], 45], 50]

list1[1][2][2][1] = 3500
print(list1)

#print pattern
rows = 5
x = 0
for i in range(rows, 0, -1):
    x += 1
    for j in range(1, i+1):
        print(x, end=' ')
    print('\r')
