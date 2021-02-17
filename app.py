from flask import Flask, request, render_template, jsonify
import sys
import test

app = Flask(__name__)
app.static_folder = 'static'

#Homepage
@app.route('/')
def index():
    return render_template('index.html')

#Takes in the query, location, and food/restaurant button
#and passes this information into a function (i.e. test_function)
@app.route('/update', methods=['POST'])
def my_form_post():
    text = request.form.get('querybox')
    loc = request.form.get('location')
    foodbtn = request.form.get('foodButton')
    oof = test.test_function(text, loc, foodbtn)
    return jsonify({'result':'success', 'data': oof})
