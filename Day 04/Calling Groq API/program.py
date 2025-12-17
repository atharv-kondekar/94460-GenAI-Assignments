import json
import requests
import dotenv
import time
import os

dotenv.load_dotenv()

api = os.getenv("api")

url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization" : f"Bearer {api}",
    "content-type" : "application/json"
}

while True:
    user = input("Human : ")

    if user == "exit":
        break

    req_data = {
        "model" : "llama-3.3-70b-versatile",
        "messages" :[
            {
                "role" : "user",
                "content" : user
            }
        ],
    }

    time1 = time.perf_counter()
    response = requests.post(url,data=json.dumps(req_data),headers=headers)
    time2 = time.perf_counter()
    res=response.json()

    print(res["choices"][0]["message"]["content"])

    print(f"Time Required : {time2-time1}")