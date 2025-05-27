from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Docker on Amazon Linux 2!\n"
