from flask import Flask, flash, render_template, redirect, request
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
mysql = MySQLConnector(app, 'email_val')
app.secret_key = '12345'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():

    query1 = 'insert into emails (email, created_at, updated_at) values (:email, now(), now())'
    
    query2 = "select email from emails"

    data = {
        'email': request.form['email']
    }

    if not EMAIL_REGEX.match(data['email']):
        flash('Please enter a valid email address')
        return redirect('/')

    emails = mysql.query_db(query2)

    for i in emails:       
        if i['email'] == data['email']:
            flash('Email has already been entered please enter another email')
            return redirect('/')
    else:
        mysql.query_db(query1, data)
        return redirect('/emails')

@app.route('/emails')
def email():
    query = "select email from emails"

    emails = mysql.query_db(query)

    return render_template('emails.html', all_emails = emails)

app.run(debug=True)