"""
This script will help understand the use of numbers in Python.
"""
print("-" * 50)
num1 = input("Enter first number: ")    # accept from the user; returns a str
num1 = float(num1)                      # convert num1 from str to float; reassign to num1

num2 = float(input("Enter second number: "))

total = num1 + num2     # sum if a builtin function; do not use as variable

print(f"sum of {num1!r} and {num2!r} is {total!r}")
