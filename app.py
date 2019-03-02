# -*- coding: utf-8 -*-
import json
from flask import Flask, request, render_template

app = Flask(__name__)

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
