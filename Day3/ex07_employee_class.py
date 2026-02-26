class Employee:
    def __init__(self, **kwargs):
        self._id = kwargs.get('id')
        self._name = kwargs.get('name')
        self._email = kwargs.get('email')
        self._salary = kwargs.get('salary')

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value
