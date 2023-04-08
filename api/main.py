from flask import Flask, render_template, request, jsonify
import math
from math import floor

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('miscellaneous.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    sets = int(request.form['sets'])
    byte_blocks = int(request.form['byte_blocks'])
    hex_string = request.form['hex_string'].split(',')

    results = []

    for i in hex_string:
        an_integer = int(i.strip(), 16)

        offset = floor(an_integer % byte_blocks)
        index = (floor(an_integer / byte_blocks) % sets)
        tag = floor(floor(an_integer / byte_blocks) / sets)

        results.append({'offset': offset, 'index': index, 'tag': hex(tag)})

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
