from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello Redis!"

if __name__ == "__main__":
    application.run()
