# -*- coding: utf-8 -*-
import json
from flask import Flask, request, render_template

app = Flask(__name__)

donations = [
    {'username': 'annonymous', 'amount': 3},
]

@app.route('/')
def index():
    return render_template('index.html', donations=donations)

@app.route('/api/donate', methods=['POST',])
def donate():
    data = request.get_json()

    entry = {}
    entry['username'] = data['username']
    entry['amount'] = data['amount']

    donations.append(entry)

    return json.dumps({'status': 'successful'})
