# -*- coding: utf-8 -*-
import json
import sqlite3
from flask import Flask, request, render_template

usercon = sqlite3.connect('users.db')
app = Flask(__name__, static_url_path='/static')

donations = [
]

@app.route('/')
def index():
    return render_template('index.html', donations=donations)

@app.route('/api/donate', methods=['POST',])
def donate():
    data = request.get_json(force=True)

    entry = {}
    entry['timestamp'] = data['timestamp']
    entry['change'] = data['change']

    donations.append(entry)

    return json.dumps({'status': 'successful'})

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        # Redner the page.
        return render_template('login.html')
    else:
        pass

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')

    elif request.method == 'POST':

        c = usercon.cursor()

        c.execute('''CREATE TABLE users (nvarchar(319) email, nvarchar(32) pswrd)''')


@app.route('/charities', methods=['GET' ,])
def charities_page():
    return render_template('Charities.html')

if __name__ == '__main__':
    app.run(debug=True)
