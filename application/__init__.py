from flask import Flask
from flask_pymongo import PyMongo


# create the app
app = Flask(__name__)
# local mongodb uri
app.config["MONGO_URI"] = "mongodb://localhost:27017/blogsite"

# Atlas connection
# app.secret_key = "1random2string3"
# app.config["MONGO_URI"] = "mongodb+srv://sidvjsingh:c2pXPjr26wK5a3kj@mongodb.enotrvk.mongodb.net/codersblog?retryWrites=true&w=majority"

# create the extension and initialize it
mongo = PyMongo(app)
db = mongo.db


from application import routes