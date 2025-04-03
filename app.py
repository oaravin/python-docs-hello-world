from flask import Flask
import datetime
app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return f"Hello, World! The current time is {current_time}."
