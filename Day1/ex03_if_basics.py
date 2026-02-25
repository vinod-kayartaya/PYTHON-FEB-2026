"""
This script helps understand the use of `if-else` statements.

USECASE: Accept student's marks (0 to 100)
If valid, print PASS or FAIL based on the marks. >=40 is PASS
If invliad (<0 or >100), print an error message

Exit codes:
0 -> success
1 -> user entered a str
2 -> user input was outside range
"""

from my_utils import line

line()
marks = int(input("Enter student's marks: "))

if marks < 0 or marks > 100:
    print("Invalid value. Marks must be between 0 and 100. ")
    exit(2)  # signals the interpreter to quit and pass the exit code to the OS

if marks < 40:
    print("Student has failed!")
else:
    print("Student has passed the exam")

line()
