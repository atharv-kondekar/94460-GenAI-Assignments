import requests
import json
url = "https://jsonplaceholder.typicode.com/posts"
# Data to send
new_post = {
    "title": "My New Post",
    "body": "This is the content of my new post",
    "userId": 1
}
# Send with custom headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer your_security_token"
}
response = requests.post(
    url, 
    data=json.dumps(new_post),
    headers=headers
)

print(f"\nCustom headers status: {response.status_code}")
print(response.json())