from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
import sqlalchemy
import requests
import os
from create_db import create_db
from datetime import datetime

# создается БД
create_db()
engine = create_engine("mysql+pymysql://user:12345@localhost/database")
Base = declarative_base()


# модели таблиц
class InfoLogs(Base):
    __tablename__ = 'info_logs'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    api_url = sqlalchemy.Column(sqlalchemy.String(length=255))
    success = sqlalchemy.Column(sqlalchemy.Integer)
    success_result = sqlalchemy.Column(sqlalchemy.String(length=1000))
    error = sqlalchemy.Column(sqlalchemy.String(length=500))


class Result(Base):
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


Base.metadata.create_all(engine)
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

# отправка запроса и фото

# ваша папка
path_dir = './photo'

# ваш урл
url1 = 'http://127.0.0.1:8000/api'
url2 = 'http://127.0.0.1:8000/api2'

# отправляет фото по 1 штуке на роут
for filename in os.listdir(path_dir):
    with open(os.path.join(path_dir, filename), 'rb') as file:
        files = [
            ('images', (filename, file, 'image/jpg'))
        ]
        request = requests.post(url1, files=files)
        # запись в БД
        log = InfoLogs(
            api_url=url1,
            success=1 if request.status_code == 200 else 0,
            success_result=request.json(),
            error=request.status_code if request.status_code != 200 else None
        )
        result = Result(
            api_url=url1,
            timestamp=datetime.now(),
            processing_time=request.json()['processing_time'],
            success=1 if request.status_code == 200 else 0,
            series=request.json()['document']['series'],
            number=request.json()['document']['number'],
            department=request.json()['document']['department'],
            code=request.json()['document']['code'],
            date_of_issue=request.json()['document']['date_of_issue'],
            gender=request.json()['document']['gender'],
            birthplace=request.json()['document']['birthplace'],
            patronymic=request.json()['document']['patronymic'],
            first_name=request.json()['document']['first_name'],
            last_name=request.json()['document']['last_name'],
            bdate=request.json()['document']['bdate'],
            type_doc=request.json()['document']['type_doc'],
        )
        session.add(result)
        session.add(log)
        session.commit()
