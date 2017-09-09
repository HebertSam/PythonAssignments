from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = '12345'

@app.route('/')


def index():
    return render_template('index.html')

@app.route('/bob', methods=['POST'])
def process():
    
    session['location'] = request.form['location']
    session['favlang'] = request.form['FavLang']
    session['name']= request.form['name']

    
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html', firstName=session['name'], location=session['location'], favlang=session['favlang'])

app.run(debug=True)