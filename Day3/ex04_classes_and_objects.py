from my_utils import line

class Book:
    def __init__(self):
        self.title = 'Let us C'
        self.author = 'Yashwant Kanitkar'
        self.price = 1299

    # one of the magic functions of an object
    # automatically called when an object is treated as str
    # e.g, print(b1)
    def __str__(self):
        return f'Book(title={self.title!r}, author={self.author!r}, price={self.price!r})'

if __name__ == '__main__':
    line()
    b1 = Book()
    b2 = Book()
    print(b1)
    print(b2)