from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Why don't scientists trust atoms? Because they make up everything!"
