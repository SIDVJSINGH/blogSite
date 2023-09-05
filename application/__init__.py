from flask import Flask
from flask_pymongo import PyMongo

import json

# local_server = False
# with open("config.json", "r") as file:
#     params = json.load(file)["params"]
#
# create the app
app = Flask(__name__)
# if local_server:
#     app.config["MONGO_URI"] = params["local_uri"]
# else:
#     app.config["MONGO_URI"] = params["atlas_uri"]

app.config["MONGO_URI"] = "mongodb://sidvjsingh:c2pXPjr26wK5a3kj@mongodb.mongodb.net/codersblog?authSource=admin"
# create the extension and initialize it
mongo = PyMongo(app)
# for local
db = mongo.db.blogcontacts
# for atlas
# db = mongo.db.blogcontacts


from application import routes
