from books import Book
from user import User
from author import Author

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []
    
    def add_book(self, title, author, genre, pub_date, availability='Available'):
        new_book = Book(title, author, genre, pub_date, availability)
        self.books.append(new_book)
        print(f"Book '{title}' added.")
    
    def borrow_book(self, user_id, book_title):
        user = self.get_user_by_id(user_id)
        if user:
            for book in self.books:
                if book.title == book_title and book.available == 'Available':
                    book.set_availability('Not Available')
                    user.borrow_book(book_title)
                    print(f"Book '{book_title}' borrowed by user {user_id}.")
                    return
            print(f"Book '{book_title}' is not available for borrowing.")
        else:
            print(f"User with ID {user_id} not found.")
    
    def return_book(self, user_id, book_title):
        user = self.get_user_by_id(user_id)
        if user:
            for book in self.books:
                if book.title == book_title and book.available == 'Not Available':
                    book.set_availability('Available')
                    user.return_book(book_title)
                    print(f"Book '{book_title}' returned by user {user_id}.")
                    return
            print(f"User {user_id} has not borrowed this book.")
        else:
            print(f"User with ID {user_id} not found.")
            
    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                print(book)
                return
        print(f"Book '{title}' not found.")
    
    def display_all_books(self):
        if not self.books:
            print("There are currently no books in the library.")
            return
        print("Available Books:")
        for book in self.books:
            print(book)
    
    def add_user(self, name, user_id):
        new_user = User(name, user_id)
        self.users.append(new_user)
        print(f"User '{name}' added successfully.")
        
    def get_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None
    
    def display_user_details(self, user_id):
        user = self.get_user_by_id(user_id)
        if user:
            print(f"User ID: {user.user_id}")
            print(f"Name: {user.name}")
            print(f"Borrowed Books: {user.get_borrowed_books()}")
        else:
            print(f"User with ID {user_id} not found.")
    
    def display_all_users(self):
        if not self.users:
            print("There are currently no users in the library.")
            return
        print("Users:")
        for user in self.users:
            print(f"User ID: {user.get_library_id()}, Name: {user.get_name()}")

    def add_author(self, name, biography):
        new_author = Author(name, biography)
        self.authors.append(new_author)
        print(f"Author '{name}' added successfully!")

    def display_author_details(self, name):
        for author in self.authors:
            if author.get_name() == name:
                print(author)
                return
        print(f"Author '{name}' not found.")

    def display_all_authors(self):
        if not self.authors:
            print("There are currently no authors in the library.")
            return
        print("Authors:")
        for author in self.authors:
            print(author)