from flask import Flask

app = Flask(__file__)


@app.get("/")
def index():
    return "Welcome to Flask test_runner_app!"
