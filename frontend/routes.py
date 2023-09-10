from flask import Blueprint, render_template, render_template_string

import backend.displaying as dis

body = Blueprint('body', __name__)

@body.route('/')
def helloWorld():
    img_b64 = dis.plotToImg()

    html = f'<img src="data:image/png;base64,{img_b64}">' 
    return render_template(['index.html', html])

@body.route('/layout')
def layout():
    return render_template('layout.html')

@body.route('/plot')
def plot():

    img_b64 = dis.plotToImg()

    html = f'<img src="data:image/png;base64,{img_b64}">' 
    return render_template_string(html)