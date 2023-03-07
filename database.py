from pymongo import MongoClient
import os

# Change information here
MONGOUSER = "mongo"
MONGOPASSWORD = "7ttkSOoWJ9zRZ2NGdtAm"
MONGOGOHOST = "containers-us-west-53.railway.app"
MONGOPORT = 7181

client = MongoClient(os.getenv("mongodb://${{ MONGOUSER }}:${{ MONGOPASSWORD }}@${{ MONGOHOST }}:${{ MONGOPORT }}"))

db = client.get_default_database()

