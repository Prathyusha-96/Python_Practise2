import json
data = {"key1" : "value1", "key2" : "value2"}
new_data = json.dumps(data)
print(type(new_data))

#Access the value of key2 from the following JSON
data = """{"key1" : "value1", "key2" : "value2"}"""
jsondata = json.loads(data)
print(jsondata["key2"])

sampleJson = {"key1": "value1", "key2": "value2", "key3": "value3"}
new_json = json.dumps(sampleJson, indent = 2 , separators=(',', '='))
print(new_json)

#Sort JSON keys in and write them into a file
sampleJson = {"id" : 1, "name" : "value2", "age" : 29}

with open('sample.json', 'w') as f:
    new_json = json.dump(sampleJson, f, indent=2, sort_keys = True)
print(new_json)

#Access the nested key ‘salary’ from the following JSON
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
data = json.loads(sampleJson)
print(data['company']['employee']['payble']['salary'])

#Convert the following Vehicle Object into JSON
import json
from json import JSONEncoder
class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

class vechileEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

json_data = json.dumps(vehicle, indent=2, cls = vechileEncoder)
print(json_data)