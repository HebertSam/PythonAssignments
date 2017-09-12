from flask import Flask, render_template, redirect, request, flash, session
import re
import datetime


app = Flask(__name__)
app.secret_key = '12345'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASS_REGEX = re.compile(r'^[a-zA-Z0-9]{8,}')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():


    for i in request.form:
        print i
        if len(request.form[i]) < 1:
            flash('Please fill out all fields')
            return redirect('/')

    if not EMAIL_REGEX.match(request.form['email']):
        flash('Please enter a valid email address')
        return redirect('/')

    elif not PASS_REGEX.match(request.form['password']):
        flash('Your password must be 8 characters and include 1 capital letter and 1 number')
        return redirect('/')
    
    elif request.form['password'] != request.form['confirm']:
        flash('Your password did not match please try again')
        return redirect('/')

    else:
        session['firstName'] = request.form['firstName']
        session['lastName'] = request.form['lastName']
        session['email'] = request.form['email']
        session['password'] = request.form['password']

        return redirect('/userinfo')

@app.route('/userinfo')
def user():
    return render_template('user.html')

app.run(debug=True)