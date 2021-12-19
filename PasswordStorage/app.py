from flask import Flask, request, render_template
import controller

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")


def validPassword(password):
    return (len(password) >= 8) & (sum(character.isdigit() for character in password) > 2)


@app.route('/register', methods=["POST"])
def register():
    data = request.get_json()
    email = data["email"]
    password = data["password"]
    if validPassword(password):
        controller.register(email, password)
        print("Registration completed, welcome to PasswordStorage!")
        return "OK"
    else:
        print("Password must be at least 8 length, including at least 2 digits")
        return "BAD"


@app.route('/login', methods=["POST"])
def login():
    data = request.get_json()
    email = data["email"]
    password = data["password"]
    if controller.login(email, password):
        print("Logging in completed, welcome to PasswordStorage!")
        return "OK"
    else:
        print("User credentials invalid!")
        return "BAD"


if __name__ == '__main__':
    controller.createUsers()
    app.run()
