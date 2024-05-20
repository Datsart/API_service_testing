from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_tables import BASE, DataPassport
import requests
from create_db import create_db
from datetime import datetime

# создается БД
create_db()
engine = create_engine("mysql+pymysql://user:12345@localhost/database")

# модель таблицы
BASE.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# ваш урл
url = 'http://127.0.0.1:8000/api'
response = requests.get(url)
data = response.json()

def get_field(data, *keys):
    try:
        for key in keys:
            data = data[key]
        return data
    except (KeyError, TypeError):
        return None

deregistered_name_departament = get_field(data, 'Снят с регистрации', 'Название подразделения')
deregistered_code_departament = get_field(data, 'Снят с регистрации', 'Код подразделения')
deregistered_date = get_field(data, 'Снят с регистрации', 'Дата')

registered_house = get_field(data, 'Зарегистрирован', 'Дом')
registered_name_departament = get_field(data, 'Зарегистрирован', 'Название подразделения')
registered_district = get_field(data, 'Зарегистрирован', 'Район')
registered_code_departament = get_field(data, 'Зарегистрирован', 'Код подразделения')
registered_date = get_field(data, 'Зарегистрирован', 'Дата')
registered_station = get_field(data, 'Зарегистрирован', 'Пункт')
registered_region = get_field(data, 'Зарегистрирован', 'Регион')
registered_street = get_field(data, 'Зарегистрирован', 'Улица')

success = data.get('success', None)
processing_time = data.get('processing_time', None)

info = DataPassport(
    deregistered_name_departament=deregistered_name_departament,
    deregistered_code_departament=deregistered_code_departament,
    deregistered_date=deregistered_date if deregistered_date else None,
    registered_house=registered_house,
    registered_name_departament=registered_name_departament,
    registered_district=registered_district,
    registered_code_departament=registered_code_departament,
    registered_date=registered_date if registered_date else None,
    registered_station=registered_station,
    registered_region=registered_region,
    registered_street=registered_street,
    success=success,
    processing_time=processing_time
)
session.add(info)
session.commit()
