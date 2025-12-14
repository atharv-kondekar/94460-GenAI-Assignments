import requests
import json
url="https://jsonplaceholder.typicode.com/posts"

response = requests.get(url + "?userId=1")

print(f"Sattus Code : {response.status_code}")
print(f" Headers : {response.headers}")

data = response.json()

print(data)

print(f"\n{json.dumps(data,indent=4)}")