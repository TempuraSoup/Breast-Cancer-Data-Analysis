from flask import Blueprint, render_template, render_template_string, request

import backend.displaying as dis

body = Blueprint('body', __name__)

@body.route('/', methods=['GET', 'POST'])
def helloWorld():
    selectedAgeRange = None
    ageRange = request.form.get('ageRange')

    img_b64 = dis.plotToImg(ageRange)

    html = f'<img src="data:image/png;base64,{img_b64}">' 
    return render_template('index.html', selectedAgeRange=ageRange) + render_template_string(html)