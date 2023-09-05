import pymongo
# Create a connection string to your MongoDB Atlas cluster.
connection_string = "mongodb://sidvjsingh:c2pXPjr26wK5a3kj@mongodb.mongodb.net/codersblog?authSource=admin"
# Create a MongoClient object.
client = pymongo.MongoClient(connection_string)
# Get the database object for the "test" database.
db = client.test
# Get the collection object for the "users" collection.
collection = db.users
# Insert a document into the "users" collection.
collection.insert_one({"name": "John Doe"})
# Find all documents in the "users" collection.
documents = collection.find()
# Print the documents to the console.
for document in documents:
    print(document)
