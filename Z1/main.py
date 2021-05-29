import requests
import json

url = 'https://getpantry.cloud/apiv1/pantry/3ab3757e-2586-4248-8cd5-843b30ae8ab8/basket/stefan2'
student = json.load(open("student.json"))

x = requests.post(url, json = student)

print(x.text)
