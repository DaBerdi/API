import requests
import json
endpoint_device = 'https://api.weather.yandex.ru/v2/informers?lat=55.75396&lon=37.620393&extra=true'
headers = {'X-Yandex-API-Key': '7db1ea84-a07c-4bfc-937a-bf45c29adca0'}
r_dev = requests.get(endpoint_device, headers=headers, verify=False)
print(r_dev)
j_dev = json.loads(r_dev.text)
print(json.dumps(j_dev, indent=4))

with open('weather.json', 'w') as f:
    json.dump(j_dev, f)

