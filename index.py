from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world() -> str:
    return "<p>Hello, World!</p>"
