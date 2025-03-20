class LibraryUtility:
    def __init__(self):
        pass

    def show_menu(self):
        """Display the Library Management System menu."""
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. List Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Exit")
        
        return input("Your choice: ").strip()

    def handle_choice(self, choice, book_manager):
        """Handle user's choice from the menu."""
        if choice == "1":
            title = input("Book title: ").strip()
            author = input("Author: ").strip()
            
            try:
                year = int(input("Year: ").strip())
                pages = int(input("Page count: ").strip())
                
            except ValueError:
                print("Invalid input for year or page count. Please enter valid integers.")
                
                return

            result = book_manager.add_book(title, author, year, pages)
            print(result)

        elif choice == "2":
            books = book_manager.get_books()
            
            if isinstance(books, list) and books:
                print("\nBooks in the Library:")
                
                for idx, book in enumerate(books, start=1):
                    print(f"ID: {idx}, Book Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Page Count: {book['pages']}")
                    
            else:
                print(books)

        elif choice == "3":
            title = input("Book title to update: ").strip()
            new_author = input("New author: ").strip()
            
            try:
                new_year = int(input("New year: ").strip())
                new_pages = int(input("New page count: ").strip())
                
            except ValueError:
                print("Invalid input for new year or page count. Please enter valid integers.")
                
                return

            result = book_manager.update_book(title, new_author, new_year, new_pages)
            print(result)

        elif choice == "4":
            title = input("Book title to delete: ").strip()
            result = book_manager.delete_book(title)
            print(result)

        elif choice == "5":
            print("Exiting the system...")

        else:
            print("Invalid choice, please try again.")
