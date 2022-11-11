import json
people_string = '''
{
    "people": [
    {
        "name" : "john deo",
        "phone": "235-452-685",
        "emails":["johndeo@gmail.com", "john-deo@company.com"],
        "has_license": false
    },
    {
        "name":"jan smith",
        "phone": "235-692-157",
        "emails": null,
        "has_license":true
    }

    ]
}
'''
data = json.loads(people_string)
# print(type(data))
# print(type(data['people']))

# print(data)
for person in data['people']:
    # print (person['name'])
    del person['phone']

new_string = json.dumps(data, indent=2, sort_keys=True )
print(new_string)