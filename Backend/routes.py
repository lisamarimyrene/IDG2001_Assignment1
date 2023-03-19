''' Nice tutorial: https://towardsdatascience.com/creating-restful-apis-using-flask-and-python-655bad51b24 ''' 

# Flask, render_template, request
from flask import Flask, render_template, request
import json
import html
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


# Source https://stackoverflow.com/questions/62906140/displaying-json-in-the-html-using-flask-and-local-json-file 
with open ('../Database/vcard.json', r) as vcardfile:
    data = vcardfile.read()

# Route to see the json vcard file
@app.route('/results')
def results():
    return render_template('index.html', title="page", jsonfile=json.dumps(data))

@app.route('/results/id')
def resultUer():
    return # user


# Just a standard if that is needed in every flask application
if __name__ == '__main__':
    app.run(debug=True)


app.run()
