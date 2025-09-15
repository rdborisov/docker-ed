from flask import Flask
from redis import Redis
import socket

app = Flask(__name__)
redis = Redis(host='redis', port=6379)


@app.route("/")
def hello_world():
    count = redis.incr('hits')
    return f"<p>Hello, World!</p> {socket.gethostname()} <p> seen: {count}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8000", debug=True)