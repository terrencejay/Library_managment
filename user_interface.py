from library_management_system import Library

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")
        main_choice = input("Enter your choice (1-4): ")

        if main_choice == "1":
            while True:
                print("\nBook Operations:")
                print("1. Add a new book")
                print("2. Borrow a book")
                print("3. Return a book")
                print("4. Search for a book")
                print("5. Display all books")
                print("6. Back to Main Menu")
                book_choice = input("Enter your choice (1-6): ")
                if book_choice == "1":
                    title = input("Enter book title: ")
                    author = input("Enter author name: ")
                    genre = input("Enter genre: ")
                    pub_date = input("Enter publication date: ")
                    library.add_book(title, author, genre, pub_date)
                elif book_choice == "2":
                    user_id = input("Enter user ID: ")
                    book_title = input("Enter book title to borrow: ")
                    library.borrow_book(user_id, book_title)
                elif book_choice == "3":
                    user_id = input("Enter user ID: ")
                    book_title = input("Enter book title to return: ")
                    library.return_book(user_id, book_title)
                elif book_choice == "4":
                    title = input("Enter book title to search: ")
                    library.searvh_book(title)
                elif book_choice == "5":
                    library.display_all_books()
                elif book_choice == "6":
                    break
                else:
                    print("Invalid choice. Please try again.")
        
        elif main_choice == "2":
            while True:
                print("\nUser Operations:")
                print("1. Add a new user")
                print("2. Display user details")
                print("3. Display all users")
                print("4. Back to Main Menu")
                user_choice = input("Enter your choice (1-4): ")
                if user_choice == "1":
                    user_id = input("Enter user ID: ")
                    name = input("Enter user name: ")
                    library.add_user(user_id, name)
                elif user_choice == "2":
                    user_id = input("Enter user ID to display details: ")
                    library.display_user_details(user_id)
                elif user_choice == "3":
                    library.display_all_users()
                elif user_choice == "4":
                    break
                else:
                    print("Invalid choice. Please try again.")
        
        elif main_choice == "3":
            while True:
                print("\nAuthor Operations:")
                print("1. Add a new author")
                print("2. Display author details")
                print("3. Display all authors")
                print("4. Back to Main Menu")
                author_choice = input("Enter your choice (1-4): ")
                if author_choice == "1":
                    name = input("Enter author name: ")
                    biography = input("Enter author biography: ")
                    library.add_author(name, biography)
                elif author_choice == "2":
                    name = input("Enter author name to display details: ")
                    library.display_author_details(name)
                elif author_choice == "3":
                    library.display_all_authors()
                elif author_choice == "4":
                    break
                else:
                    print("Invalid choice. Please try again.")
        
        elif main_choice == "4":
            print("Exiting Library Management System...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()