from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/contacts')
def get_contacts():
    return CONTACTS


if __name__ == '__main__':
    app.run()

