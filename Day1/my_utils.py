"""
Custom utility functions are defined here
"""

def line(ch='-', size=80):
    """
    Prints a line which is made up of 80 hyphens
    """
    if not isinstance(ch, str):
        print("1st argument to line() function must be a str")
    elif not isinstance(size, int):
        print("2nd argument to line() function must be an int")
    else:
        print(ch * size)

def is_leap(year: int) -> bool:
    # year must be divisible by 400
    # year must be divisible by 4 and not by 100
    return year % 400 == 0 or (year % 4 ==0 and year % 100 != 0)


def max_days(month:int, year:int) -> int:
    # TODO: validate if the inputs are valid values for month and year
    if month == 2:
        return 29 if is_leap(year) else 28

    if month in (4, 6, 9, 11):
        return 30
    
    return 31


def is_valid_date(dt:str) -> bool:
    # dt must be a str
    if not isinstance(dt, str): 
        return False
    
    # dt must contain 2 slashes ('/') e.g, '23/2/2026'
    if dt.count('/') != 2: 
        return False
    
    # since there are 2 '/' symbols, the split function returns a list of 3 units
    # e.g, ['23', '2', '2026'] or ['vinod', 'kumar', 'bangalore']
    d, m, y = dt.split('/')

    if d.isdigit() == False or m.isdigit() == False or y.isdigit() == False:
        return False
    
    d, m, y = int(d), int(m), int(y)

    if y < 0: 
        return False
    
    if m < 1 or m > 12: 
        return False

    md = max_days(m, y)
    if d < 1 or d > md: 
        return False
    
    return True


def print_multiplication_table(num, /, limit=10):
    for i in range(1, limit+1):
        print(f'{num} X {i} = {num*i}')


def factorial(num, /):
    if isinstance(num, str) and num.isdigit():
        num = int(num)
    else:
        raise TypeError("Invalid datatype. Must be an int")

    if not isinstance(num, int):
        raise TypeError("Invalid datatype. Must be an int")
    
    if num < 0:
        raise ValueError("I don't know the factorial of negative input")
    
    f = 1
    while num > 0:
        f *= num
        num -= 1

    return f
