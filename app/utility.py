import logging

class LibraryUtility:
    def __init__(self):
        self._setup_logging()

    def _setup_logging(self):
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
        self.logger = logging.getLogger(__name__)

    def show_menu(self):
        """Display the Library Management System menu."""
        self.logger.info("Library Management System")
        self.logger.info("1. Add Book")
        self.logger.info("2. List Books")
        self.logger.info("3. Update Book")
        self.logger.info("4. Delete Book")
        self.logger.info("5. Exit")
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
                self.logger.error("Invalid input for year or page count. Please enter valid integers.")
                return

            result = book_manager.add_book(title, author, year, pages)
            self.logger.info(result)

        elif choice == "2":
            books = book_manager.get_books()
            if isinstance(books, list) and books:
                self.logger.info("\nBooks in the Library:")
                for idx, book in enumerate(books, start=1):
                    self.logger.info(f"ID: {idx}, Book Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Page Count: {book['pages']}")
            else:
                self.logger.info(books)

        elif choice == "3":
            title = input("Book title to update: ").strip()
            new_author = input("New author: ").strip()
            try:
                new_year = int(input("New year: ").strip())
                new_pages = int(input("New page count: ").strip())
            except ValueError:
                self.logger.error("Invalid input for new year or page count. Please enter valid integers.")
                return

            result = book_manager.update_book(title, new_author, new_year, new_pages)
            self.logger.info(result)

        elif choice == "4":
            title = input("Book title to delete: ").strip()
            result = book_manager.delete_book(title)
            self.logger.info(result)

        elif choice == "5":
            self.logger.info("Exiting the system...")

        else:
            self.logger.warning("Invalid choice, please try again.")
