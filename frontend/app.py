
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return "<h1>Hello World Bruh</h1>"