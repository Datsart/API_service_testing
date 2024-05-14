from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api', methods=['POST', 'GET'])
def api():
    if request.method == 'POST':
        # data = request.get_json()
        return jsonify('success'), 200


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
