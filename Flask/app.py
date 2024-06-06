from flask import Flask, render_template, request, session
import os
from openai import OpenAI
import re

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a secret key for session storage


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/file', methods=['GET', 'POST'])
def file():
    if request.method == 'POST':
        file = request.files['file']
        file.save(os.path.join('uploads', file.filename))
        print(file.read())
        return 'File uploaded successfully'
    # return render_template('file.html')


if __name__ == '__main__':
    app.run(debug=True)