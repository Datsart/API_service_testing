import os
import sqlite3
import requests

conn = sqlite3.connect('database.db')

cursor = conn.cursor()
'''Отправляет файлы на роут'''
upload_url = 'http://83.239.206.206:5005/api/set_transcribe'
audio_dir = 'test_audio'

for filename in os.listdir(audio_dir):
    file_path = os.path.join(audio_dir, filename)
    with open(file_path, 'rb') as file:
        print(filename)
        cursor.execute('INSERT INTO name_audio (name) VALUES (?)', (filename,))
        conn.commit()
        files = {'file': (filename, file, 'audio/mpeg')}
        response = requests.post(upload_url, files=files)
