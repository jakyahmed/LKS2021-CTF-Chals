from flask import Flask, render_template
from flask import render_template_string
from flask import request
import re

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        ex = request.form['expression']
        if ex == None or ex == '':
            return 'tidak ada data yang dikirim'
        
        res = "Hasil: {}".format('{{' + ex + '}}')

        return render_template('index.html', result = render_template_string(res))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)