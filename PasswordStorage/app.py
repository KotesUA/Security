import flask
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():  # put application's code here
    return flask.render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    data = request.get_json()
    email = data["email"]
    password = data["password"]

    # TODO: make database and hashing

    return "Registration completed, welcome to PasswordStorage!"

@app.route('/login', methods=["GET", "POST"])
def login():
    data = request.get_json()
    email = data["email"]
    password = data["password"]

    # TODO: make login via database

    return "Logging in completed, welcome to PasswordStorage!"


if __name__ == '__main__':
    app.run()
