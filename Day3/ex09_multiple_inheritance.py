from my_utils import dirr, line

class Person:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        print(f"Person.__init__() was called with {kwargs}")

    def print(self):
        print("Printing from Person")

class Employee(Person):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.empid = kwargs.get('empid')
        self.salary = kwargs.get('salary')
        print(f"Employee.__init__() was called with {kwargs}")

    def print(self):
        print("Employee from Employee")

class Student(Person):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rollno = kwargs.get('rollno')
        self.gpa = kwargs.get('gpa')
        print(f"Student.__init__() was called with {kwargs}")

    def print(self):
        
        print("Printing from Student")

class WorkingStudent(Employee, Student):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Employee.__init__(self, **kwargs)
        # Student.__init__(self, **kwargs)
        self.department = kwargs.get('department')
        print(f"WorkingStudent.__init__() was called with {kwargs}")

    def print(self):
        super().print()
        print("Printing from WorkingStudent")

if __name__ == '__main__':
    line()
    print(f'{WorkingStudent.mro() = }')
    ws = WorkingStudent()
    ws.print()
    line()