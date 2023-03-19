# Flask, render_template, request
from flask import Flask, render_template, request
import os

# Set the flask app
app = Flask(__name__)
api = Api(app)


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


# Run app
app.run()