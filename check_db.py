from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["blog_database"]
posts_collection = db["posts"]

cursor = posts_collection.find()
for document in cursor:
    print(document)

# # Delete all documents from the collection
# result = posts_collection.delete_many({})
# print(f"Deleted {result.deleted_count} documents from the collection.")
