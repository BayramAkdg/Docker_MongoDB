import logging

class LibraryUtility:
    def __init__(self):
        self._setup_logging()

    def _setup_logging(self):
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
        self.logger = logging.getLogger(__name__)

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
            title = input("Book title: ")
            author = input("Author: ")
            year = int(input("Year: "))
            pages = int(input("Page count: "))
            book_manager.add_book(title, author, year, pages)
            
        elif choice == "2":
            books = book_manager.get_books()
            
            if books:
                print("\nBooks in the Library:")
                
                for idx, book in enumerate(books, start=1):
                    print(f"ID: {idx}, Book Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Page Count: {book['pages']}")
                    
        elif choice == "3":
            title = input("Book title to update: ")
            new_author = input("New author: ")
            new_year = int(input("New year: "))
            new_pages = int(input("New page count: "))
            book_manager.update_book(title, new_author, new_year, new_pages)
            
        elif choice == "4":
            title = input("Book title to delete: ")
            book_manager.delete_book(title)
        elif choice == "5":
            print("Exiting the system...")
        else:
            print("Invalid choice, please try again.")
