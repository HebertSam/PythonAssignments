from flask import Flask, render_template, redirect

app = Flask(__name__)

dev = True


@app.route('/')

def start():
    return redirect('/main')

@app.route('/main')
def begin():
    return render_template('index.html')
    

@app.route('/main/left')
def left():
    return render_template('left.html')

@app.route('/main/right')
def right():
    return render_template('right.html')


app.run(debug=dev)

