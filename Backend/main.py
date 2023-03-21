from flask import Flask, render_template, request
import json
import html
import os

# Set the flask app
app = Flask(__name__)
api = Api(app)



''' APIS '''

# This is our API's
# Test get
@app.route('/', methid)
def get_users():
    user_id = request.args.get('id')
    # implement code to retrieve and return user data
    return jsonify(user)

# Get
@app.route('/api/users')
def get_users():
    user_id = request.args.get('id')
    # implement code to retrieve and return user data
    return jsonify(user)


# Post
@app.route('/api/users', methods=['POST'])
def create_user():
    user_data = request.json
    # implement code to create and return user data
    return jsonify(user)


''' ROUTES '''

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

# Run app
app.run()