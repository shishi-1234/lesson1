import requests
import json
web = 'http://itchild.solidhost.ru/'
result = requests.get(web)
print(result)
print('Код ответа от сервера:', result.status_code)

print('Тескт овета')
main_url1 = f'{web}?page_id=5/'
result1 = requests.post(main_url1, data={'name':'Musia', 'breed': 'siam', 'age': '20'})
print(result1)