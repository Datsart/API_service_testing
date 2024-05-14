from flask import Flask, jsonify, request
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from datetime import datetime
from create_db import create_db
import json

Base = declarative_base()


class Result(Base):
    __tablename__ = 'results'
    id = Column(Integer, primary_key=True)
    result = Column(String)
    timestamp = Column(DateTime, default=datetime.now)


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)


@app.route('/api/result', methods=['POST'])
def post():
    '''Принимает результаты'''
    data = request.get_json()
    # Преобразуем словарь в строку
    result_str = json.dumps(data)
    # запись в БД
    result_obj = Result(
        result=result_str,
    )
    session.add(result_obj)
    session.commit()
    return 'success'


if __name__ == '__main__':
    create_db()
    app.run(host='127.0.0.1', port=5000, debug=True)
