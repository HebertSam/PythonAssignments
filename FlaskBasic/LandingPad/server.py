from flask import Flask, render_template, redirect

app = Flask(__name__)

dev = True

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojos')
def dojos():
    return render_template('dojos.html')

app.run(debug=dev)