from my_utils import line, remove_names_starting_with

line()
names = ['Vinod', 'Shyam', 'Vikram', 'John', 'Jane', 'Vijay', 'Vishal']  # list object with values
cities = list()  # using the constructor; cannot initialize values
cities.append('Bangalore')
cities.append('Chennai')
friends = 'Ramesh,Vinay,Harish,James,Kishore'
friends_list = friends.split(',')  # split method returns a list
print(f'{names = }')
print(f'{cities = }')
print(f'{friends_list = }')

nums = (123, 94, 288, 599)  # nums is a tuple (read-only collection)
nums = list(nums)  # create a new list using the tuple
print(f'{nums = }')

# list methods: append, clear, copy, count, extend, index, 
# insert, pop, remove, reverse, sort

# heterogenous list
emp = [1120, 'Kiran Rao', 'ADMIN', 40000, 1198, True]
print(f'{emp = }')

names.append('Suresh') # adds 'Suresh' to the end of the list
names.insert(0, 'Mahesh') # inserts 'Mahesh' at index 0; pushes rest
names.insert(100000, 'Raghu')  # same as append, if index is out of range
print(f'{names = }')

print(f'{len(names) = }')
print(f'{names[3] = }')
# print(f'{names[100000] = }')  # raise IndexError

# what is the index of a name 'John'?
print(f'{names.index("John") = }')
# what is the index of a name 'Praveen' (not in the list)?
# print(f'{names.index("Praveen") = }') # ValueError: 'Praveen' is not in list

name = 'John'
if name in names:
    print(f'names.index({name!r}) = {names.index(name)}')
    names.remove(name)  # deletes an element by value
    # if the name does not exist, raises ValueError
    print(f'after deleting {name!r}, {names = }')
else:
    print(f'{name!r} does not belong to the list `names`')

# avoid using these methods, as they reverse/sort the list in place
# (you lose original values)
# names.reverse()
# names.sort()

# Insted, use the builtins functions reversed and sorted
reversed_names = list(reversed(names))
sorted_names = sorted(names)

print(f'{reversed_names = }')
print(f'{sorted_names = }')
print(f'{names = }')

# remove_names_starting_with(names, 'V')
# print(f'{names = }')
line()