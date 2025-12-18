import streamlit as st
import requests
import dotenv
import json
import os

dotenv.load_dotenv()

api = os.getenv("groq_api")   # make sure no space in key name
url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api}",
    "Content-Type": "application/json"
}


local_api ="dummy"
local_url="http://127.0.0.1:1234/v1/chat/completions"

local_headers={
    "Authorization":f"Bearer {local_api}",
    "content-type":"application/json"
}

st.title("Multiple Chatbots")
with st.sidebar:
    st.header("Switch API")
    mode = st.selectbox("Select Models", ["Local API", "Cloud Based API"])

msg = st.chat_input("Ask Anything...")

if msg:
    if mode == "Cloud Based API":
        
        req_data = {
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {"role": "user", "content": msg}
            ]
        }

        with st.chat_message("user"):
            st.write(msg)
        response = requests.post(
            url,
            headers=headers,
            json=req_data   # better than data=json.dumps
        )

        #HTTP-level check
        if response.status_code != 200:
            st.error(f"HTTP Error {response.status_code}")
            st.code(response.text)
        else:
            res = response.json()

            # API-level check
            if "choices" not in res:
                st.error("Groq API Error")
                st.json(res)
            else:
                with st.chat_message("assistant"):
                    st.write(res["choices"][0]["message"]["content"])

    #For the Local API 

    elif mode == "Local API":
        req_data ={
            "model":"meta-llama-3.1-8b-instruct",
            "messages":[
                {
                    "role":"user",
                    "content":msg
                }
            ]
        }
        with st.chat_message("user"):
            st.write(msg)

        response=requests.post(local_url,headers=local_headers,json=req_data)

        if response.status_code!=200:
            st.error(f"HTTP Error {response.status_code}")
            st.code(response.text)            
        else:
            res=response.json()

            if "choices" not in res :
                st.error("API Error")
                st.json(res)
            
            else:
                with st.chat_message("assistant"):
                    st.write(res["choices"][0]["message"]["content"])
