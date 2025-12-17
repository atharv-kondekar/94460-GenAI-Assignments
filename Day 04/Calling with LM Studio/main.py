import os
import requests
import json
import time
import dotenv

dotenv.load_dotenv()
url = "http://127.0.0.1:1234/v1/chat/completions"

api=os.getenv("api")

headers = {
    "content-type" : "application/json",
    "Authorization":f"Bearer {api}"
}

while True:
    user = input("Enter Something : ")

    if user == "exit":
        break

    req_data = {
        "model" :"meta-llama-3.1-8b-instruct",
        "messages":[
            {
                "role" : "user",
                "content":user
            }
        ],
    }

    time1=time.perf_counter()
    response = requests.post(url,headers=headers,data=json.dumps(req_data))
    time2=time.perf_counter()

    resp = response.json()
    print(resp["choices"][0]["message"]["content"])
    print(f"Time required: {time2-time1:.2f} sec")