class Book:
    """Represents a book with a title, author, and availability status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False

    def check_out(self):
        if not self.__is_checked_out:
            self.__is_checked_out = True
            print(f'"{self.title}" has been checked out.')
        else:
            print(f'"{self.title}" is already checked out.')

    def return_book(self):
        if self.__is_checked_out:
            self.__is_checked_out = False
            print(f'"{self.title}" has been returned.')
        else:
            print(f'"{self.title}" was not checked out.')

    def is_checked_out(self):
        return self.__is_checked_out


class Library:

    def __init__(self):
        self.__books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.__books.append(book)
            print(f'Book "{book.title}" by {book.author} added to the library.')
        else:
            print("Only Book instances can be added.")

    def check_out_book(self, title):
        for book in self.__books:
            if book.title == title:
                book.check_out()
                return
        print(f'Book "{title}" not found in the library.')

    def return_book(self, title):
        for book in self.__books:
            if book.title == title:
                book.return_book()
                return
        print(f'Book "{title}" not found in the library.')

    def list_available_books(self):
        available_books = [book for book in self.__books if not book.is_checked_out()]
        if not available_books:
            print("No available books at the moment.")
        else:
            print("Available books:")
            for book in available_books:
                print(f'- "{book.title}" by {book.author}')
