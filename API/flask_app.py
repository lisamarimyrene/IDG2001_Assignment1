''' Nice tutorial: https://towardsdatascience.com/creating-restful-apis-using-flask-and-python-655bad51b24 ''' 

# Flask, render_template, request
from flask import Flask, render_template, request
import os

# Set the flask app
app = Flask(__name__)
api = Api(app)


# Homepage, find the form
@app.route('/')
def home():
    return render_template('../Frontend/index.html')

# Route when uploading file from form
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save(file.filename)
    return 'File uploaded successfully!'

# Just a standard if that is needed in every flask application
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