import json

#json string
employee = '{"name": "john", "id":123456, "post":"developer", "pay": 50000}'

#convert to python object
data = json.loads(employee)
print(type(data))
print('\n')

#converting python dict to json
data_1 = json.dumps(data, indent=2)
print(type(data_1))

# Python program showing that
# json support different primitive
# types

#list conersion to array
print(json.dumps(["hello", "world"]))

#tuple conversion to array
print(json.dumps(("hello", "world")))

#string conersion to string
print(json.dumps('Hii'))

#int conversion to number
print(json.dumps(123))

#float
print(json.dumps(12.5))

#boolean
print(json.dumps(True))
print(json.dumps(False))

#None
print(json.dumps(None))







# from urllib.request import urlopen

# with urlopen('https://finance.yahoo.com/webservise/v1/symbols/allcurencies/qoute?format=json') as response:
#     source = response.read()
# data = json.loads(source)
# print(json.dumps(data))
