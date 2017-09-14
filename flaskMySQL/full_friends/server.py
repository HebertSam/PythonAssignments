from flask import Flask, render_template, redirect, session, flash, url_for, request
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'full_friendsdb')

@app.route('/')
def index():
    query = "select * from users"
    friend = mysql.query_db(query)


    return render_template('index.html', all_friends = friend)

@app.route('/friends', methods=['POST'])
def friends():

    query = "insert into users (first_name, last_name, age, created_at, updated_at) values (:first_name, :last_name, :age, now(), now())"

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }

    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)