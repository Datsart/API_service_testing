from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
import sqlalchemy
import requests
import os
from create_db import create_db

# создается БД
create_db()
engine = create_engine("mysql+pymysql://user:12345@localhost/database")
Base = declarative_base()


# модель таблицы
class InfoLogs(Base):
    __tablename__ = 'info_logs'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    api_url = sqlalchemy.Column(sqlalchemy.String(length=255))
    success = sqlalchemy.Column(sqlalchemy.Integer)
    success_result = sqlalchemy.Column(sqlalchemy.String(length=1000))
    error = sqlalchemy.Column(sqlalchemy.String(length=500))


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
        success = 1 if request.status_code == 200 else 0
        error = request.status_code if request.status_code != 200 else None
        log = InfoLogs(
            api_url=url1,
            success=success,
            success_result=request.json(),
            error=error
        )
        session.add(log)
        session.commit()
