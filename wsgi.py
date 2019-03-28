from flask import Flask
from redis import Redis
application = Flask(__name__)
R = Redis(host="demo-db.redis1.svc.cluster.local", port=15212)
#R = Redis()

@application.route("/")
def hello():
    return str(R.ping())

if __name__ == "__main__":
    application.run(debug=True)
