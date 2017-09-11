import random
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = '12345'

@app.route('/')
def index():
    session['num'] = random.randrange(1, 101)
    session['hint'] = ""
    print session['num']
    
    return redirect('/home')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('sucess.html')

@app.route('/process', methods=['POST'])
def process():
    session["guess"] = request.form['guess']

    if session['num'] < int(request.form['guess']):
        session['hint'] = "thats too high guess again"
    
    elif session['num'] > int(request.form['guess']):
        session['hint'] = "thats too low guess again"
    
    elif session['num'] == int(request.form['guess']):

        return redirect('/success')
    
    return redirect('/home')

@app.route('/process2', methods=["POST"])
def process2():

    if request.form['reset'] == 'reset':
        return redirect('/')
        
app.run(debug=True)