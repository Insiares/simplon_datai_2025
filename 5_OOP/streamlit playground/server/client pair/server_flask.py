from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data')

def give():
    data = { 'bonjour' : 'Bonjour à tous',
            'Bravo' : 'Bravo à tous'}
    return jsonify(data)