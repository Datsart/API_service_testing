from sqlalchemy.orm import declarative_base
import sqlalchemy

BASE = declarative_base()


class InfoLogs(BASE):
    __tablename__ = 'info_logs'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    api_url = sqlalchemy.Column(sqlalchemy.String(length=255))
    success = sqlalchemy.Column(sqlalchemy.Integer)
    success_result = sqlalchemy.Column(sqlalchemy.String(length=1000))
    error = sqlalchemy.Column(sqlalchemy.String(length=500))


# модель таблицы результатов
class Result(BASE):
    __tablename__ = 'result'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    api_url = sqlalchemy.Column(sqlalchemy.String(length=255))
    timestamp = sqlalchemy.Column(sqlalchemy.TIMESTAMP, default=sqlalchemy.func.current_timestamp())
    processing_time = sqlalchemy.Column(sqlalchemy.Integer)
    success = sqlalchemy.Column(sqlalchemy.Integer)
    series = sqlalchemy.Column(sqlalchemy.String(length=20))
    number = sqlalchemy.Column(sqlalchemy.String(length=30))
    department = sqlalchemy.Column(sqlalchemy.String(length=200))
    code = sqlalchemy.Column(sqlalchemy.String(length=15))
    date_of_issue = sqlalchemy.Column(sqlalchemy.String(length=30))
    gender = sqlalchemy.Column(sqlalchemy.String(length=10))
    birthplace = sqlalchemy.Column(sqlalchemy.String(length=150))
    last_name = sqlalchemy.Column(sqlalchemy.String(length=100))
    first_name = sqlalchemy.Column(sqlalchemy.String(length=100))
    patronymic = sqlalchemy.Column(sqlalchemy.String(length=100))
    bdate = sqlalchemy.Column(sqlalchemy.String(length=15))
    type_doc = sqlalchemy.Column(sqlalchemy.String(length=30))


# модель таблицы сравнения
class ComparisonResult(BASE):
    __tablename__ = 'comparison_result'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    # api_url = sqlalchemy.Column(sqlalchemy.String(length=255))
    timestamp = sqlalchemy.Column(sqlalchemy.TIMESTAMP, default=sqlalchemy.func.current_timestamp())
    series = sqlalchemy.Column(sqlalchemy.Integer)
    number = sqlalchemy.Column(sqlalchemy.Integer)
    department = sqlalchemy.Column(sqlalchemy.Integer)
    code = sqlalchemy.Column(sqlalchemy.Integer)
    date_of_issue = sqlalchemy.Column(sqlalchemy.Integer)
    gender = sqlalchemy.Column(sqlalchemy.Integer)
    birthplace = sqlalchemy.Column(sqlalchemy.Integer)
    last_name = sqlalchemy.Column(sqlalchemy.Integer)
    first_name = sqlalchemy.Column(sqlalchemy.Integer)
    patronymic = sqlalchemy.Column(sqlalchemy.Integer)
    bdate = sqlalchemy.Column(sqlalchemy.Integer)
    type_doc = sqlalchemy.Column(sqlalchemy.Integer)
    percentage_of_accuracy = sqlalchemy.Column(sqlalchemy.String(length=10))
