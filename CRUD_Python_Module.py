from pymongo import MongoClient
from pymongo.errors import PyMongoError


class AnimalShelterCRUD:
    """
    CRUD class for interacting with the AAC MongoDB animals collection
    """

    def __init__(self, username, password, host="localhost", port=27017):
        """Initialize MongoDB connection."""
        self.client = None
        self.database = None
        self.collection = None

        try:
            self.client = MongoClient(
                f"mongodb://{username}:{password}@{host}:{port}/?authSource=admin"
            )
            self.database = self.client["aac"]
            self.collection = self.database["animals"]
        except PyMongoError as e:
            print(f"Connection error: {e}")

    def create(self, data):
        """Insert one document. Returns True if inserted, else False."""
        if data is None or self.collection is None:
            return False

        try:
            # duplicate check (prevents inserting same animal_id twice)
            existing = self.collection.find_one({"animal_id": data.get("animal_id")})
            if existing:
                print("Record already exists. Skipping insert.")
                return False

            self.collection.insert_one(data)
            return True
        except PyMongoError as e:
            print(f"Insert error: {e}")
            return False

    def read(self, query):
        """Query documents. Returns a list of documents or an empty list."""
        if query is None or self.collection is None:
            return []

        try:
            results = self.collection.find(query)
            return list(results)
        except PyMongoError as e:
            print(f"Read error: {e}")
            return []

    def update(self, query, new_values):
        """
        Update document(s) matching query using $set new_values.
        Returns the number of documents modified.
        """
        if query is None or new_values is None or self.collection is None:
            return 0

        try:
            result = self.collection.update_many(query, {"$set": new_values})
            return result.modified_count
        except PyMongoError as e:
            print(f"Update error: {e}")
            return 0

    def delete(self, query):
        """
        Delete document(s) matching query.
        Returns the number of documents deleted.
        """
        if query is None or self.collection is None:
            return 0

        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except PyMongoError as e:
            print(f"Delete error: {e}")
            return 0