from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/<name>")
def hello_name(name):
    return f"Hello, {name}!"

@app.route("/json")
def json_response():
    return jsonify({"message": "Hello, World!"})
