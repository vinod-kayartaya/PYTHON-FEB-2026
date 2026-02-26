"""
This is a menu driven console application that allows the user to manage a book library.
Users can add/search/list/delete/edit book details.
A book detail consists of book_id, title, author, price.
Each book is represented by a tuple containing the book details in the above sequence.
A library is a list of books.

For example:

[
    (12, 'Let us C', 'Y Kanitkar', 499),
    (38, 'Life is Good', 'Robert', 999),
]

As CSV:

ID,Title,Author,Price
12,Let us C,Y Kanitkar,499
38,Life is Good,Robert,999

"""

import os

# global variable, a list of books
books = [
    (123, 'Python Unleashed, 2nd edition', 'John Doe', 1399),
    (312, 'Python Collections', 'Jane Doe', 399),
    (381, 'Mastering Python', 'John Jacob', 2999)
]

def list_all_books():
    global books  # tells the interpreter that `books` is  defined outside this function
    if len(books) == 0:
        print("No books in the library. Please add few books.")
        return
    
    print('-'*65)
    print(f'{"ID":5}{"Title":25}{"Author":25}{"Price":10}')
    print('-'*65)
    for book_id, title, author, price in books:
        print(f'{book_id:<5}{title:25}{author:25}{price:10.2f}')
    print('-'*65)
    

def delete_book():
    try:
        book_id = int(input("Enter the book id to delete: "))
    except:
        print("Invalid value for ID. Please try again")
        return
    
    found = False
    for index, book in enumerate(books):
        if book[0] == book_id:
            book_to_delete = books[index]
            print(f"Book found for id {book_id}")
            print(f"Title : {book_to_delete[1]}")
            print(f"Author: {book_to_delete[2]}")
            print(f"Price : {book_to_delete[3]}")
            choice = input("Are you sure to delte this book? (yes/no) ")
            
            if choice.lower() == 'yes':
                books.pop(index)
                print("Book deleted successfully!")
            else:
                print("Book was not deleted.")

            found = True
            break
    
    if not found:
        print("Book id not found. Please try again.")


def save_as_csv():
    csv_content = 'ID,Title,Author,Price'
    for book_id, title, author, price in books:
        csv_content += f'\n{book_id},"{title}","{author}",{price}'

    with open("books.csv", "wt") as f:
        print(csv_content, file=f)
        print("books.csv created.")

def menu() -> int:
    os.system("cls")
    print("=== Library Management App ===")
    print("===        MAIN MENU       ===")
    print("""
0. Exit
1. Add a new book details
2. List all books
3. Edit a book
4. Delete a book
5. Save as CSV file
6. Save as JSON file
          """)
    choice = input("Enter your choice: ")
    try:
        choice = int(choice)
    except:
        choice = -1

    return choice


def main():
    while True:
        ans = menu()

        if ans == 0:
            break

        if ans < 1 or ans > 6:
            print("Invalid choice. Please retry.")
        elif ans == 1:
            ...
        elif ans == 2:
            list_all_books()
        elif ans == 3:
            ...
        elif ans == 4:
            delete_book()
        elif ans == 5:
            save_as_csv()
        elif ans == 6:
            ...

        # do this before continuing the loop
        input("Hit ENTER/RETURN key to continue")
    
    # last line in the main() function
    print("Bye! Thank for using our app.")

if __name__ == '__main__':
    # call the main() function
    main()