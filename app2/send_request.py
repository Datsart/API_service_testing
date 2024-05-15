from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
import sqlalchemy
import requests
import os
from create_db import create_db
from datetime import datetime
from model_tables import BASE, InfoLogs, ComparisonResult, Result

# создается БД
create_db()
engine = create_engine("mysql+pymysql://user:12345@localhost/database")

# модель таблицы запросов


BASE.metadata.create_all(engine)
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

# отправка запроса и фото:

# ваша папка
path_dir = './photo'

# ваш урл
url1 = 'http://127.0.0.1:8000/api'
url2 = 'http://127.0.0.1:8000/api2'

# отправляет фото по 1 штуке на ОБА роута
for filename in os.listdir(path_dir):
    with open(os.path.join(path_dir, filename), 'rb') as file:
        files = [
            ('images', (filename, file, 'image/jpg'))
        ]
        request1 = requests.post(url1, files=files)
        request2 = requests.post(url2, files=files)

        # запись в БД:

        # запись состояния отправки на 1 роут
        log1 = InfoLogs(
            api_url=url1,
            success=1 if request1.status_code == 200 else 0,
            success_result=request1.json(),
            error=request1.status_code if request1.status_code != 200 else None
        )
        session.add(log1)
        session.commit()

        # запись состояния отправки на 2 роут
        log2 = InfoLogs(
            api_url=url2,
            success=1 if request2.status_code == 200 else 0,
            success_result=request2.json(),
            error=request2.status_code if request2.status_code != 200 else None
        )
        session.add(log2)
        session.commit()

        # запись пришедших данных с 1го роута
        result1 = Result(
            api_url=url1,
            timestamp=datetime.now(),
            processing_time=request1.json()['processing_time'],
            success=1 if request1.status_code == 200 else 0,
            series=request1.json()['document']['series'],
            number=request1.json()['document']['number'],
            department=request1.json()['document']['department'],
            code=request1.json()['document']['code'],
            date_of_issue=request1.json()['document']['date_of_issue'],
            gender=request1.json()['document']['gender'],
            birthplace=request1.json()['document']['birthplace'],
            patronymic=request1.json()['document']['patronymic'],
            first_name=request1.json()['document']['first_name'],
            last_name=request1.json()['document']['last_name'],
            bdate=request1.json()['document']['bdate'],
            type_doc=request1.json()['document']['type_doc'],
        )
        session.add(result1)
        session.commit()

        # запись пришедших данных со 2го роута
        result2 = Result(
            api_url=url2,
            timestamp=datetime.now(),
            processing_time=request2.json()['processing_time'],
            success=1 if request2.status_code == 200 else 0,
            series=request2.json()['document']['series'],
            number=request2.json()['document']['number'],
            department=request2.json()['document']['department'],
            code=request2.json()['document']['code'],
            date_of_issue=request2.json()['document']['date_of_issue'],
            gender=request2.json()['document']['gender'],
            birthplace=request2.json()['document']['birthplace'],
            patronymic=request2.json()['document']['patronymic'],
            first_name=request2.json()['document']['first_name'],
            last_name=request2.json()['document']['last_name'],
            bdate=request2.json()['document']['bdate'],
            type_doc=request2.json()['document']['type_doc'],
        )
        session.add(result2)
        session.commit()

        # сравнение результатов и запись схожести в БД
        series = 1 if request1.json()['document']['series'] == request2.json()['document']['series'] else 0
        number = 1 if request1.json()['document']['number'] == request2.json()['document']['number'] else 0
        department = 1 if request1.json()['document']['department'] == request2.json()['document'][
            'department'] else 0
        code = 1 if request1.json()['document']['code'] == request2.json()['document']['code'] else 0
        date_of_issue = 1 if request1.json()['document']['date_of_issue'] == request2.json()['document'][
            'date_of_issue'] else 0
        gender = 1 if request1.json()['document']['gender'] == request2.json()['document']['gender'] else 0
        birthplace = 1 if request1.json()['document']['birthplace'] == request2.json()['document'][
            'birthplace'] else 0
        patronymic = 1 if request1.json()['document']['patronymic'] == request2.json()['document'][
            'patronymic'] else 0
        first_name = 1 if request1.json()['document']['first_name'] == request2.json()['document'][
            'first_name'] else 0
        last_name = 1 if request1.json()['document']['last_name'] == request2.json()['document']['last_name'] else 0
        bdate = 1 if request1.json()['document']['bdate'] == request2.json()['document']['bdate'] else 0,
        type_doc = 1 if request1.json()['document']['type_doc'] == request2.json()['document']['type_doc'] else 0,

        # расчет точности:
        # один показатель = 8,3% так как показателей 12 -> 100 / 12 ~ 8.3
        percentage_of_accuracy = (
                                         series + number + department + code + date_of_issue + gender + birthplace + patronymic + first_name + last_name + bdate + type_doc) * 8.3
        percentage_of_accuracy = str(percentage_of_accuracy) + '%'
        accuracy = ComparisonResult(
            timestamp=datetime.now(),
            series=series,
            number=number,
            department=department,
            code=code,
            date_of_issue=date_of_issue,
            gender=gender,
            birthplace=birthplace,
            patronymic=patronymic,
            first_name=first_name,
            last_name=last_name,
            bdate=bdate,
            type_doc=type_doc,
            percentage_of_accuracy=percentage_of_accuracy
        )
        session.add(accuracy)
        session.commit()
