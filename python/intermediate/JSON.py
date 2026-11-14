import json
person={"name":"jon","age":30,"city":"new york","hasChild":False,"titled":["engi","programmer"]}
personJSON=json.dumps(person,indent=4,separators=(",",":"))

print(personJSON)
with open('person.json','w') as file:
    json.dump(person,file,indent=4)

personJSON=json.dumps(person,indent=4,sort_keys=True)
print(person)



class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age
user=User('max',27)
def encode_user(o):
    if isinstance(o,User):
        return {"name":o.name,"age":o.age,o.__class__.__name__:True}
    else:
        raise TypeError('object of type user is not json serializable')
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self,o):
       if isinstance(o,User):
            return {'name':o.name,'age':o.age,o.__class__.name__:True}
        return JSONEncoder.default(self,o)
userJSON=UserEncoder().encode(user)
print(userJSON)
def decode_user(dict):
    if User.__name__ in dict:
        return User(name=dict['name'],age=dict['age'])
    return dict
user = json.loads(userJSON,object_hook=decode_user)
print(type(user))
print(user.name)


#random numbers
