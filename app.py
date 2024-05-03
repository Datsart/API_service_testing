from flask import Flask, jsonify, request
from create_db import create_db
import sqlite3

app = Flask(__name__)


@app.route('/api/result', methods=['POST'])
def post():
    '''Принимает результаты'''
    data = request.get_json()
    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        cur.execute("INSERT INTO results (hash) VALUES (?)", (data['file_hash']))
        con.commit()
    return jsonify({'result': 'recieve',
                    'file_hash': data['file_hash']})


if __name__ == '__main__':
    create_db()
    app.run(host='127.0.0.1', port=5000, debug=True)
