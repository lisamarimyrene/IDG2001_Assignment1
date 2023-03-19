from pymongo import MongoClient
import os

# Change information here
MONGOUSER = "mongo"
MONGOPASSWORD = "7ttkSOoWJ9zRZ2NGdtAm"
MONGOGOHOST = "containers-us-west-53.railway.app"
MONGOPORT = 7181

client = MongoClient(os.getenv("mongodb://${{ MONGOUSER }}:${{ MONGOPASSWORD }}@${{ MONGOHOST }}:${{ MONGOPORT }}"))

db = client.get_default_database()


''' Found this method also, using MongoEngine instead of MongoClient, don't know what is best

https://www.mongodb.com/compatibility/mongoengine-pymongo 

# Flask with mongo db
from flask_mongoengine import MongoEngine

# Connect to mongo database 
database_name = "vCardDB"
DB_URI = "mongodb+srv://lisamarimyrene:mongodbpassword@cluster0.mub535i.mongodb.net/vCardDB?retryWrites=true&w=majority"
app.config["MONGODB_HOST"] = DB_URI 

# Set the database
db = MongoEngine()
# Put the app inside the database
db.init_app(app)

'''

'''

from pymongo import MongoClient
def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb+srv://user:pass@cluster.mongodb.net/myFirstDatabase"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['user_shopping_list']
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()

'''