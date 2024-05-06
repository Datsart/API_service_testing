import os
import requests
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from datetime import datetime
import hashlib

Base = declarative_base()


# созжаем модель таблицы
class Audio(Base):
    __tablename__ = 'audio'
    id = Column(Integer, primary_key=True)
    name_audio = Column(String)
    hash_audio = Column(String)
    timestamp = Column(DateTime, default=datetime.now)


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

upload_url = 'http://83.239.206.206:5005/api/set_transcribe'
audio_dir = 'test_audio'
# по одному файлу отправляем на указанный роут
for filename in os.listdir(audio_dir):
    file_path = os.path.join(audio_dir, filename)
    with open(file_path, 'rb') as file:
        hash_result = hashlib.md5(filename.encode()).hexdigest()
        objects = session.query(Audio).all()
        # если файл существует (проверка по хэшу) то ничего
        list_hash = [i.hash_audio for i in objects]
        if hash_result not in list_hash:
            print(filename, '- записывем')
            audio_obj = Audio(
                name_audio=filename,
                hash_audio=hash_result,
            )
            session.add(audio_obj)
            session.commit()
            # отправляем файл на указанный URL
            files = {'file': (filename, file, 'audio/mpeg')}
            response = requests.post(upload_url, files=files)
        else:
            print('Такой файл уже существует. Ничего не отправляем и не записываем')

print('\nЦикл отправки и сохранения в БД завершен')
