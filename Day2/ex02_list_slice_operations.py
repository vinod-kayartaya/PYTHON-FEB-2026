from my_utils import line

line()

nums = [10, 12, 39, 82, 855, 22, 58, 68, 1, 58]
print(f'total elements in nums = {len(nums)}')
print(f'{nums = }')
print(list(enumerate(nums)))

# accessing a single element in a list
print(f'{nums[4] = }')

# sublist consisting of 4 elements from index 3
print(f'{nums[3:7] = }')

# sublist consiting of all elements from index 4
print(f'{nums[4:] = }')

# sublist consiting of all elements before index 7
print(f'{nums[:7] = }')

name = 'Vinod Kumar'

print(f'{name[:5] = }')

# last element in a list
print(f'{nums[-1] = }')
print(f'{name[-1] = }')

# last 5 letters in my name
print(f'{name[-5:] = }')

# 3 largest values in the list `nums`
print(f'{sorted(nums)[-3:] = }')

# all elements
print(f'{nums[::] = }')
# elements at even indices
print(f'{nums[::2] = }')
# access elements at every 3rd index
print(f'{nums[::3] = }')

# nums in reverse order, but index 0 is excluded
print(f'{nums[-1:0:-1] = }')

# nums in reverse order
print(f'{nums[::-1] = }')

# reversing a str
print(f'{name[::-1] = }')


filename = 'july_customers_data.json'
basename = filename[:-5]
extension = filename[-4:]
print(f'{filename = }\n{basename = }\n{extension = }\n')

basename, _, extension = filename.partition('.')
print(f'{filename = }\n{basename = }\n{extension = }\n')


line()