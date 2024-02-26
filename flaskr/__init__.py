from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<p>welcome to strada!</p>"