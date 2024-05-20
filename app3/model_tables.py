from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

BASE = declarative_base()


class DataPassport(BASE):
    __tablename__ = 'data_passport'

    id = Column(Integer, primary_key=True, autoincrement=True)
    deregistered_name_departament = Column(String(length=300), nullable=True)
    deregistered_code_departament = Column(String(length=15), nullable=True)
    deregistered_date = Column(Date, nullable=True)
    registered_house = Column(String(length=20), nullable=True)
    registered_name_departament = Column(String(length=300), nullable=True)
    registered_district = Column(String(length=300), nullable=True)
    registered_code_departament = Column(String(length=15), nullable=True)
    registered_date = Column(Date, nullable=True)
    registered_station = Column(String(length=300), nullable=True)
    registered_region = Column(String(length=300), nullable=True)
    registered_street = Column(String(length=300), nullable=True)
    success = Column(Integer, nullable=True)
    processing_time = Column(Integer, nullable=True)
