from flask import Flask, render_template, url_for
app = Flask(__name__)
app.secret_key = '12345'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('ninja.html')

@app.route('/ninja/<color>')
def ninjaColor(color):
    ninjas = ['blue', 'orange', 'red', 'purple']
    print color
    for i in ninjas:
        print i
        if color == i:
            return render_template(color +'.html')
    else:
        return render_template('april.html')



app.run(debug=True)