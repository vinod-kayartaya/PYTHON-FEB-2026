from my_utils import line

class Book:
    def __init__(self):
        print(f'{id(self) = }')
        # `self` is the reference to the newly constructed object
        # passed by python runtime, when a new Book object is created.
        # using this variable `self`, we can add new members to the newly
        # constructed object
        self.id = None
        self.title = None
        self.author = None
        print('Book instance created')


if __name__ == '__main__':
    line()
    b1 = Book() # `new` keyword doesn't exist in python
    print(f'{id(b1) = }')
    line()
    b2 = Book()
    print(f'{id(b2) = }')
    line()

    # unline C++, Java, C# the constructor/initializer can be invoked using a variable
    # NO POINT IN DOING SO
    b2.__init__()

    # possible; but we never do these:
    # b1.title = 'Let us C'
    # b2.name = 'Life is Good'

    b2.pages = 430

    print(f'{dir(b1) = }', '\n')
    print(f'{dir(b2) = }')