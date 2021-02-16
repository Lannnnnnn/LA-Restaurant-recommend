from flask import Flask, request, render_template
import sys
import test

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form.get('querybox')
    keys = request.form.keys()
    keys = [key for key in keys]
    loc = request.form.get('location')
    oof = test.test_function(text, loc, keys)
    return render_template('index.html', data=oof)
