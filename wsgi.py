from os import getenv
from json import loads

from flask import Flask, request, render_template
from redis import Redis

application = Flask(__name__)
redis = Redis(host="demo-db.adi.svc.cluster.local", port=12345)

@application.route('/')
def form():
#    return str(redis.ping())
    return render_template('form.html')

@application.route('/', methods=['POST'])
def submit():
    print request.form
    _ = redis.rpush('form-inputs', request.form['input-text'])
    return render_template('form.html', success=True)

@application.route('/clear')
def clear():
    redis.flushdb()
    return 'DB Cleared'


if __name__ == "__main__":
    application.run()
