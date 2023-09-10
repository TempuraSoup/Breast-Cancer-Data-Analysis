from flask import Flask
from flask_cors import CORS

from .routes import body

def create_app():
    app = Flask(__name__, static_folder='staticFiles')
    CORS(app)

    app.register_blueprint(body)
    
    return app