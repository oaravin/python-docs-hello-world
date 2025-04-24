from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    """Returns a simple \"Hello, World!\" string."""
    return "Hello, World!"
