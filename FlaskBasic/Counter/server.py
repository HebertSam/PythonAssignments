from flask import Flask, redirect, render_template, session, request

app = Flask(__name__)
app.secret_key = '12345'

@app.route('/')
def index():
    
    session['num'] += 1
    
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():

    if request.form['number'] == 'add':
        session['num'] += 1
    elif request.form['number'] == 'reset':
        session['num'] = 0

    return redirect('/')


app.run(debug=True)