from flask import Blueprint, render_template

body = Blueprint('body', __name__)

@body.route('/')
def helloWorld():
    return render_template('index.html')

@body.route('/layout')
def layout():
    return render_template('layout.html')