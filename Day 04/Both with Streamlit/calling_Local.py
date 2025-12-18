import streamlit as st
import requests 
import os 
import dotenv
import time
import json 

st.title("Chat bot")

dotenv.load_dotenv()
api = "dummy - key "
url = "http://127.0.0.1:1234/v1/chat/completions"
headers = {
    "content-type":"application/json",
    "Authorization":f"Bearer {api}"
}

if "messages" not in st.session_state:
    st.session_state.messages=[]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


user_input = st.chat_input("Ask Anything : ")

if user_input:

    st.session_state.messages.append(
        {
            "role" : "user",
            "content":user_input
        }
    )

    req_data = {
        "model":"meta-llama-3.1-8b-instruct",
        "messages":st.session_state.messages
    }

    response = requests.post(url,headers=headers,data=json.dumps(req_data))
    resp = response.json()

    ai= resp["choices"][0]["message"]["content"]


    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":ai
        }
    )

    with st.chat_message("assistant"):
            st.write(ai)

    st.rerun()