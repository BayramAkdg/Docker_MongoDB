from pymongo.errors import PyMongoError

class BookManager:
    def __init__(self, database):
        self.db = database
        self.collection = self.db.db["books"]

    def add_book(self, title, author, year, pages):
        """Add a new book to the library."""
        try:
            if not title or not author:
                print("Title and author must be provided.")
                
                return "Title and author must be provided."

            result = self.collection.insert_one({"title": title, "author": author, "year": year, "pages": pages})

            if result.inserted_id:
                print(f"Book added: {title} by {author}, {year}, {pages} pages.")
                
                return f"Book '{title}' by {author} has been added!"
                
            else:
                print("Failed to add book.")
                
                return "Failed to add book."
        except PyMongoError as e:
            print(f"Error adding book: {e}")
            
            return f"Error adding book: {e}"

    def get_books(self):
        """List all books in the library."""
        try:
            books = list(self.collection.find())
            
            if books:
                print(f"Listing {len(books)} books.")
                
                return books
            else:
                print("No books found in the library.")
                
                return "No books found in the library."
                
        except PyMongoError as e:
            print(f"Error retrieving books: {e}")
            
            return f"Error retrieving books: {e}"

    def update_book(self, title, new_author, new_year, new_pages):
        """Update an existing book."""
        try:
            result = self.collection.update_one(
                {"title": title},
                {"$set": {"author": new_author, "year": new_year, "pages": new_pages}}
            )
            
            if result.matched_count:
                print(f"Book updated: {title} -> {new_author}, {new_year}, {new_pages} pages.")
                
                return f"Book '{title}' updated."
            else:
                print(f"Book with title '{title}' not found.")
                
                return f"Book with title '{title}' not found."
                
        except PyMongoError as e:
            print(f"Error updating book: {e}")
            
            return f"Error updating book: {e}"

    def delete_book(self, title):
        """Delete a book from the library."""
        try:
            result = self.collection.delete_one({"title": title})
            
            if result.deleted_count:
                print(f"Book deleted: {title}")
                
                return f"Book '{title}' deleted."
            else:
                print(f"Book with title '{title}' not found.")
                
                return f"Book with title '{title}' not found."
        except PyMongoError as e:
            print(f"Error deleting book: {e}")
            return f"Error deleting book: {e}"
