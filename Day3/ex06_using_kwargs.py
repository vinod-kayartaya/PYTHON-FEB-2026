from my_utils import line

class Book:
    def __init__(self, **kwargs):
        self.title = kwargs.get('title')
        self.author = kwargs.get('author')
        self.__price = kwargs.get('price')

    # for each private member variable, create a getter and a setter
    # @property marks a function as a readable property (like a variable)
    # e.g, print(b1.price)
    @property
    def price(self):
        return self.__price
    
    # a setter is for a given readable property
    # @<property>.setter marks the `price` function as a setter, which takes
    # 2 parameters - 1st one is the invoking object (LHS), 2nd one is the RHS
    # e.g, b1.price = 5000   --> b1 is the invoking object, 5000 is the value
    @price.setter
    def price(self, value):
        if value is not None and type(value) not in (int, float):
            raise TypeError('Invalid type for price. Must be int or float')
        
        if type(value) in (int, float):
            if value < 0 or value > 99999:
                raise ValueError('Invalid value for price. Must be between 0 and 99999')
        
        self.__price = value


    def __str__(self):
        return f'Book(title={self.title!r}, author={self.author!r}, price={self.__price!r})'
    
    def print(self):
        # `self` here is the invoking object; for example, if b1.print() is called, self == b1
        print('Here is the book details:')
        print(f'Title     : {self.title}')
        print(f'Author    : {self.author}')
        print(f'Price     : {self.__price}')
        line(size=50)


if __name__ == '__main__':
    line()
    b1 = Book(title='Let us C', author='Y Kanitkar', price=1299)
    b2 = Book(title='Python crash course', author='Eric Matthe', price=1500)

    print(b1)
    print(b2)
    line()

    b2.price = 499  # triggers invocation of the setter method

    b1.print()
    b2.print()
    b3 = Book(title='Python Unleashed', author='John Doe')
    b3.print()
    