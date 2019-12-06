class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.patron = None
        self.wait_list = []

    def __repr__(self):
        return 'Title: {}\nAuthor: {}\nPatron: {}\nWait List: {}'.format(
            self.title, self.author, self.patron, self.wait_list
        )


class Patron:
    def __init__(self, name):
        self.name = name
        self.books_requested = 0

    def borrow_book(self, book):
        if self.books_requested == 3 or self == book.patron or self in book.wait_list:
            return

        self.books_requested += 1

        if book.patron is None:
            book.patron = self
        else:
            book.wait_list.append(self)

    def return_book(self, book):
        if self.books_requested == 0 or self != book.patron:
            return

        self.books_requested -= 1

        if book.wait_list != []:
            # The wait list is a FIFO (first in first out) queue
            book.patron = book.wait_list[0]
            del book.wait_list[0]
        else:
            book.patron = None

    def __repr__(self):
        return '{}: {} book(s)'.format(
            self.name,
            self.books_requested
        )


if __name__ == '__main__':
    book1 = Book('B1', 'A1')
    book2 = Book('B2', 'A2')
    book3 = Book('B3', 'A3')
    book4 = Book('B4', 'A4')
    patron1 = Patron('P1')
    patron2 = Patron('P2')
    patron3 = Patron('P3')

    books = (book1, book2, book3, book4)
    patrons = (patron1, patron2, patron3)

    for patron in patrons:
        patron.borrow_book(book1)

    for book in books:
        patron1.borrow_book(book)
        patron3.borrow_book(book)

    patron2.borrow_book(book4)

    for book in books:
        print(book)
        print()

    print('-'*20)

    patron1.return_book(book1)  # book goes to P2
    patron3.return_book(book2)  # nothing happens, B2 has patron P1, not P3
    patron1.return_book(book3)
    patron2.return_book(book4)

    for book in books:
        print(book)
        print()
