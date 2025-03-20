import logging
from pymongo import MongoClient


class Database:
    def __init__(self, db_url="mongodb://mongo:27017/", db_name="library"):
        self.db_url = db_url
        self.db_name = db_name
        self.client = None
        self.db = None
        self._setup_logging()

    def _setup_logging(self):
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
        self.logger = logging.getLogger(__name__)

    def connect(self):
        """Establish connection to MongoDB and retrieve the database."""
        try:
            self.client = MongoClient(self.db_url)
            self.db = self.client[self.db_name]
            self.logger.info(f"Successfully connected to MongoDB at {self.db_url}.")
            
        except Exception as e:
            self.logger.error(f"Error connecting to MongoDB: {e}")
            
            raise

    def close(self):
        """Close the MongoDB connection."""
        try:
            if self.client:
                self.client.close()
                self.logger.info("MongoDB connection closed.")
                
        except Exception as e:
            self.logger.error(f"Error closing MongoDB connection: {e}")
