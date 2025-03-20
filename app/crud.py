import logging
from pymongo.errors import PyMongoError

class BookManager:
    def __init__(self, database):
        self.db = database
        self.collection = self.db.db["books"]
        self._setup_logging()

    def _setup_logging(self):
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
        self.logger = logging.getLogger(__name__)

    def add_book(self, title, author, year, pages):
        """Add a new book to the library."""
        try:
            self.collection.insert_one({"title": title, "author": author, "year": year, "pages": pages})
            self.logger.info(f"Book added: {title} by {author}, {year}, {pages} pages.")
            
        except PyMongoError as e:
            self.logger.error(f"Error adding book: {e}")

    def get_books(self):
        """List all books in the library."""
        try:
            books = list(self.collection.find())
            if books:
                self.logger.info(f"Listing {len(books)} books.")
                return books
            
            else:
                self.logger.warning("No books found in the library.")
                
                return []
            
        except PyMongoError as e:
            self.logger.error(f"Error retrieving books: {e}")
            
            return []

    def update_book(self, title, new_author, new_year, new_pages):
        """Update an existing book."""
        try:
            result = self.collection.update_one(
                {"title": title},
                {"$set": {"author": new_author, "year": new_year, "pages": new_pages}}
            )
            
            if result.matched_count:
                self.logger.info(f"Book updated: {title} -> {new_author}, {new_year}, {new_pages} pages.")
                
            else:
                self.logger.warning(f"Book with title {title} not found.")
                
        except PyMongoError as e:
            self.logger.error(f"Error updating book: {e}")

    def delete_book(self, title):
        """Delete a book from the library."""
        try:
            result = self.collection.delete_one({"title": title})
            
            if result.deleted_count:
                self.logger.info(f"Book deleted: {title}")
                
            else:
                self.logger.warning(f"Book with title {title} not found.")
                
        except PyMongoError as e:
            self.logger.error(f"Error deleting book: {e}")
