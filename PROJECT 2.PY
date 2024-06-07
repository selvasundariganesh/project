class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Borrowed: {'Yes' if self.is_borrowed else 'No'}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return True
        return False

    def list_books(self):
        for book in self.books:
            print(book)

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def borrow_book(self, title):
        book = self.search_book(title)
        if book and not book.is_borrowed:
            book.is_borrowed = True
            return True
        return False

    def return_book(self, title):
        book = self.search_book(title)
        if book and book.is_borrowed:
            book.is_borrowed = False
            return True
        return False


library = Library()
library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))

print("All books in the library:")
library.list_books()

print("\nSearch for '1984':")
print(library.search_book("1984"))

print("\nBorrow '1984':")
library.borrow_book("1984")
library.list_books()

print("\nReturn '1984':")
library.return_book("1984")
library.list_books()

print("\nRemove '1984':")
library.remove_book("1984")
library.list_books()
