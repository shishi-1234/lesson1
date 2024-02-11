import requests
import json
web = 'https://petstore.swagger.io/'
result = requests.get(web)
print(result)
print('Код ответа от сервера:', result.status_code)

print('Тескт овета')
main_url = f'{web}ru/feed'
result = requests.get(web)
data = result.json()
print(data)
