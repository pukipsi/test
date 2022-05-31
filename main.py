import requests


response = requests.get('http://yandex.ru')
print(response.status_code)
