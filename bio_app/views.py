from flask import Flask, render_template, url_for, request
import sys
import os

app = Flask(__name__)
app.config.from_object('config')

from .utils import gen_bio

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/result/')
def result():
    domaine = request.args.get('domaine')
    created_by = request.args.get('created_by')
    build = request.args.get('build')
    return (render_template('result.html', methods=['GET', 'POST'], gen_bio=gen_bio, domaine = domaine, created_by = created_by, build = (build=='True')))

if __name__ == "__main__":
    app.run()
