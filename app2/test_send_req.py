import requests
import os

path_dir = './photo'
url = 'http://127.0.0.1:8000/api'
# отправляет фото по 1 штуке на роут
for filename in os.listdir(path_dir):
    with open(os.path.join(path_dir, filename), 'rb') as file:
        files = [
            ('images', (filename, file, 'image/jpg'))
        ]
        request = requests.post(url, files=files)
        print(request.json())
