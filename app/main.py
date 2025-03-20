from database import Database
from crud import BookManager
from utility import LibraryUtility

class LibraryApp:
    def __init__(self):
        self.db = Database()
        self.db.connect()
        self.book_manager = BookManager(self.db)
        self.utility = LibraryUtility()

    def run(self):
        """Run the Library Management System."""
        while True:
            choice = self.utility.show_menu()
            
            if choice == "5":
                self.db.close()
                
                break
            self.utility.handle_choice(choice, self.book_manager)

if __name__ == "__main__":
    app = LibraryApp()
    app.run()
