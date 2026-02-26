from my_utils import line

class Book:
    def __init__(self, title=None, author=None, price=None):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f'Book(title={self.title!r}, author={self.author!r}, price={self.price!r})'


if __name__ == '__main__':
    line()
    b1 = Book('Let us C', 'Y Kanitkar', 1299)
    b2 = Book('Python crash course', 'Eric Matthe')

    print(b1)
    print(b2)
    line()