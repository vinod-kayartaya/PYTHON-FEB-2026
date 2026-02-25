from my_utils import line
import math

line()
nums = [10, 12, 39, 82, 855, 22, 58, 68, 1, 58]


# When we need to 
# 1. convert/transform elements of one list into another
# 2. filter a list
# 3. combination of both

# [element_to_append for each_element from collection]
squares = [n*n for n in nums]
square_roots = [math.sqrt(num) for num in nums]

print(f'{nums = }')
print(f'{squares = }')
print(f'{square_roots = }')

names = ['vinod kumar', 'SHYAM SUNDAR', 'Suresh Kamath', 'rohit', 'RAHUL']
names = [name.title() for name in names]
print(f'{names = }')

nums_str = '10, 409, 683, 38, 689, 70, 223, 82, 855, 22, 58, 68'
nums = nums_str.split(',')
print(f'{nums = }')

nums = [int(n) for n in nums_str.split(',')]
print(f'{nums = }')

# [element_to_append for each_element from collection if condition_satisfied]
even_nums = [n for n in nums if n%2 == 0]
odd_nums = [a for a in nums if a%2]

print(f'{even_nums = }')
print(f'{odd_nums = }')

emps = 'vinod;vinay;anil;arun;ramesh;vishal;vikram;rajesh;vineet'
print(f'{emps = }')

emps1 = ','.join([e.upper() for e in emps.split(';') if e.startswith('v')])
print(f'{emps1 = }')

line()
