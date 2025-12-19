import streamlit as st
from langchain_groq import ChatGroq
import dotenv
import os
import time 

dotenv.load_dotenv()
st.title("ChatBot")

api= os.getenv("groq_api")

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=api
)

if "messages" not in st.session_state :
    st.session_state.messages=[]

for msg in st.session_state.messages:
    if msg["role"]=="user":
        with st.chat_message("user"):
            st.write(msg["content"])
    else:
        st.markdown(msg["content"])

user = st.chat_input("Ask Anything ...... ")

if user : 

    st.session_state.messages.append(
        {
            "role" : "user",
            "content":user
        }
    )

    with st.chat_message("user"):
        st.write(user)
    
    answer = ""
    box=st.empty()

    
    for chunk in llm.stream(user):
        answer+=chunk.content
        time.sleep(0.01)
        box.markdown(answer)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )
    