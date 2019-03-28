from flask import Flask
from redis import Redis
application = Flask(__name__)
R = Redis(host="web1.redis1.svc.cluster.local", port=15638)

@application.route("/")
def hello():
    return R.ping()

if __name__ == "__main__":
    application.run(debug=True)
