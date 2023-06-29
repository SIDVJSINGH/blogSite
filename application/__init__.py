from flask import Flask
from flask_pymongo import PyMongo


# create the app
app = Flask(__name__)
# local mongodb uri
app.config["MONGO_URI"] = "mongodb://localhost:27017/blogsite"
# create the extension and initialize it
mongo = PyMongo(app)
db = mongo.db


from application import routes