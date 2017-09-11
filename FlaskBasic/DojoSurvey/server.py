from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)
app.secret_key = '12345'

@app.route('/')


def index():
    session['location'] = None
    session['favlang'] = None
    session['name'] = None
    session['comments'] = None

    return render_template('index.html')

@app.route('/bob', methods=['POST'])
def process():
    
    session['location'] = request.form['location']
    session['favlang'] = request.form['FavLang']
    if len(request.form['name']) < 1:
        flash('Name can not be empty')
        return redirect('/')
    else:
        session['name']= request.form['name']

    if len(request.form['comment']) > 120:
        flash('Sorry you comment is too long it can only be 120 characters')
        return redirect('/')
    else:
        session['comments'] = request.form['comment']
    
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html', firstName=session['name'], location=session['location'], favlang=session['favlang'], comment=session['comments'])

app.run(debug=True)