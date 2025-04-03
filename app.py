from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({"message": "Hello, World!", "timestamp": timestamp})
