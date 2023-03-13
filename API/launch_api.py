# Flask, render_template, request
from flask import Flask, render_template, request
# Flask with mongo db
from flask_mongoengine import MongoEngine

import os

# Set the flask app
app = Flask(__name__)

# Connect to mongo database 
database_name = "vCardDB"
DB_URI = "mongodb+srv://lisamarimyrene:mongodbpassword@cluster0.mub535i.mongodb.net/vCardDB?retryWrites=true&w=majority"
app.config["MONGODB_HOST"] = DB_URI

# Set the database
db = MongoEngine()
# Put the app inside the database
db.init_app(app)


@app.route('/')
def home():
    return render_template('../Frontend/index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save(file.filename)
    return 'File uploaded successfully!'

if __name__ == '__main__':
    app.run(debug=True)


'''
# Routes (old)
@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/contacts')
def get_contacts():
    return CONTACTS
'''