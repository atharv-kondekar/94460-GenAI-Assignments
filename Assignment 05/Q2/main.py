## 2. ⁠Connect to Groq and Gemini AI using REST api. Send same prompt and compare results. Also compare the speed.
import time
import requests
import os
import dotenv
import json

dotenv.load_dotenv()

#Groq
api= os.getenv("groq_api")
url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization" : f"Bearer {api}",
    "content-type" : "application/json"
}

# Gemini 
gem = os.getenv("gemini_ai")
gem_url=(  "https://generativelanguage.googleapis.com/v1/"
    "models/gemini-pro:generateContent"
    f"?key={gem}")

header = {
    "content-type" : "application/json"
}


print(" --------------- Using th Groq ---------------- ")
while True : 
    user = input("Ask Anything : ")

    if user == "exit" :
        break

    req_data= {
        "model" : "llama-3.3-70b-versatile",
        "messages":[
            {
                "role":"user",
                "content":user
            }
        ]
    }

    time1=time.perf_counter()
    response = requests.post(url,headers=headers,data=json.dumps(req_data))
    time2=time.perf_counter()

    res = response.json()

    print("AI : ",res["choices"][0]["message"]["content"])
    print(f"Time for the Groq : {time2-time1}")


    print("------------using Gemini -----------")
    req ={
        "contents": [
            {
                "parts": [
                    { "text": user }
                ]
            }
        ]
    }

    time3=time.perf_counter()
    result=requests.post(gem_url,headers=header,data=json.dumps(req))
    time4=time.perf_counter()

    re=result.json()

   # print("AI :", re["candidates"][0]["content"]["parts"][0]["text"])
    print(re)
    print(time3)
    print(time4)
    print(f"time for Gemini ={time4-time3} ")






