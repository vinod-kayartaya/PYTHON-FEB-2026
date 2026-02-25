"""
A `dict` is a collection of key-value pairs.
Each key-value is called an item.
In Java/C# they are equivalent to Map<K,V> and in JavaScript it is equivalent to an object
Keys must be immutable, and are unique.
Unlike the list, which is accessible using index, dict elements are accessed using keys

"""

from my_utils import line
from pprint import pprint

line()

# create a dict using constructor
p1 = dict(name='Vinod', age=52, married=True, phones=['9731424784'])
# create a dict using {} notation.
p2 = {"name": "Shyam", "age": 53, "married": False}
# keys can be any immutable types
p3 = {45: 'Rohit', 18: 'Virat', 10: 'Sachin'}

print(f'{p1 = }')
print(f'{p2 = }')
print(f'{p3 = }')

# access a value using key (may result in KeyError)
print(f'{p1["name"] = }')
# print(f'{p1["email"] = }')  # `email` is not a key in p1
print(f'{p1.get("phones") = }')
print(f'{p1.get("email") = }')
print(f'{p1.get("email", "nobody@xmpl.com") = }')

# add a new key/value pair (or replace an existing one)
p1["email"] = "vinod@vinod.co"
p1["city"] = "Bangalore"
p1["name"] = "Vinod Kumar K"

print(f'{p1 = }')

# iterate over the `dict`: keys(), values(), items()
print(f'{p1.keys() = }')
print(f'{p1.values() = }')
print(f'{p1.items() = }')

line()

print("p1 has these keys:")
for key in p1.keys():
    print(key)

line()

print("p1 has these values:")
for val in p1.values():
    print(val)

line()

print("p1 has these items:")
for item in p1.items():
    print(item)


line()

removed_item = p1.popitem()

print(f'{removed_item = }')
print(f'{p1 = }')

if 'email' in p1:   # same as --> if 'email' in p1.keys():
    deleted_email = p1.pop('email')
    print(f'{deleted_email = }')
    print(f'{p1 = }')
else:
    print('no key called "email"')

line()

point1 = dict(x=12, y=34)
point2 = dict(y=66, z=44)

print(f'{point1 = }')
print(f'{point2 = }')

point1.update(point2)

print(f'{point1 = }')
print(f'{point2 = }')

line()

emp_keys = ['id', 'name', 'salary', 'department', 'mgr_id']
emp1 = dict.fromkeys(emp_keys, '')
print(f'{emp1 = }')

emp1_vals = [1928, 'Ramesh Iyer', 45000, 'ADMIN', 2812]

# zip(emp_keys, emp1_vals)
# --> [('id', 1928), ('name', 'Ramesh Iyer'), .. .. ..]

emp1 = dict(zip(emp_keys, emp1_vals))
print(f'{emp1 = }')