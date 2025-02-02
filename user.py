class User:
    def __init__(self, name, library_id, borrowed_books=None):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = borrowed_books if borrowed_books is not None else []

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_library_id(self):
        return self.__library_id

    def set_library_id(self, library_id):
        self.__library_id = library_id

    def get_borrowed_books(self):
        return self.__borrowed_books

    def set_borrowed_book(self, book_title):
        self.__borrowed_books.append(book_title)

    def return_book(self, book_title):
        if book_title in self.__borrowed_books:
            self.__borrowed_books.remove(book_title)

    def __str__(self):
        return f"Name: {self.__name}\nLibrary ID: {self.__library_id}\nBorrowed Books: {', '.join(self.__borrowed_books)}"