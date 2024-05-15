from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api', methods=['POST', 'GET'])
def api():
    if request.method == 'POST':
        # data = request.get_json()
        return jsonify({
            "success": 1,
            "document": {
                "series": "11 04",
                "number": "000000",
                "department": "ОТДЕЛОМ ВНУТРЕННИХ ДЕЛ ОКТЯБРЬСКОГО ОКРУГА ГОРОДА АРХАНГЕЛЬСКА",
                "code": "292-000",
                "date_of_issue": "17.12.2004",
                "gender": "МУЖ",
                "birthplace": "ГОР АРХАНГЕЛЬСК",
                "patronymic": "АЛЕКСАНДРОВИЧ",
                "first_name": "ЕВГЕНИЙ",
                "last_name": "ИМЯРЕК",
                "bdate": "12.09.1982",
                "type_doc": "passport"
            },
            "processing_time": 10
        }
        ), 200


@app.route('/api2', methods=['POST', 'GET'])
def api2():
    if request.method == 'POST':
        # data = request.get_json()
        return jsonify({
            "success": 1,
            "document": {
                "series": "11 04",
                "number": "000000",
                "department": "ОТДЕЛОМ ВНУТРЕННИХ ДЕЛ ОКТЯБРЬСКОГО ОКРУГА ГОРОДА АРХАНГЕЛЬСКА",
                "code": "292-000",
                "date_of_issue": "17.12.2004",
                "gender": "МУЖ",
                "birthplace": "ГОР АРХАНГЕЛЬСК",
                "patronymic": "АЛЕКСАНДРОВИЧ",
                "first_name": "ЕВГЕНИЙ",
                "last_name": "ИМЯРЕК",
                "bdate": "12.09.1982",
                "type_doc": "passport"
            },
            "processing_time": 10
        }
        ), 200


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
