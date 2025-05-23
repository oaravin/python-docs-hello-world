from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

# Why do programmers prefer dark mode?
# Because light attracts bugs!
