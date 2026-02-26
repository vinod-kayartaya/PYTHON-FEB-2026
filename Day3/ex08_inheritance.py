class Person:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.city = kwargs.get('city')
        self.email = kwargs.get('email')

    def print(self):
        print(f'Name     = {self.name}')
        print(f'City     = {self.city}')
        print(f'Email    = {self.email}')


class Employee(Person):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.empid = kwargs.get('empid')
        self.salary = kwargs.get('salary')

    def print(self):
        print(f'ID       = {self.empid}')
        super().print()
        print(f'Salary   = {self.salary}')

    
if __name__ == '__main__':
    e1 = Employee(empid=1122, name='Vishal', city='Chennai', salary=50000, email='vishal@xmpl.com')
    print(f'{dir(e1) = }')

    e1.print()