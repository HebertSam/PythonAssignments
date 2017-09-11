import random
from flask import Flask, redirect, request, render_template, session
from datetime import datetime
import time

app = Flask(__name__)
app.secret_key = '12345'

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except KeyError:
        session['my_gold'] = 0
        session['activ'] = []
        return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    localTime = time.asctime( time.localtime(time.time()))
    print localTime
    print request.form['get_gold']
    if request.form['get_gold'] == 'farm':
        farm = random.randint(10, 21)
        session['my_gold'] += farm
        session['activ'].append('Earned {} golds from the farm: {}'.format(farm, localTime))
    elif request.form['get_gold'] == 'cave':
        cave = random.randint(5, 11)
        session['my_gold'] += cave
        session['activ'].append('Earned {} golds from the cave: {}'.format(cave, localTime))
    elif request.form['get_gold'] == 'house':
        house = random.randint(2, 6)
        session['my_gold'] += house
        session['activ'].append('Earned {} golds from the house: {}'.format(house, localTime))
    elif request.form['get_gold'] == 'casino':
        casino = random.randint(-50, 51)
        session['my_gold'] += casino
        if casino > 0:
            session['activ'].append('Earned {} golds from the casino: {}'.format(casino, localTime))
        else:
            session['activ'].append('Lost {} golds from the casino: {}'.format(casino, localTime))
    elif request.form['get_gold'] == 'reset':
        session['my_gold'] = 0
        session['activ'] = []




    return redirect('/')
    
app.run(debug=True)