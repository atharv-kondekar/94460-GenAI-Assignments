import streamlit as st
import time
import os
from langchain.chat_models import init_chat_model
import dotenv

dotenv.load_dotenv()

st.title("Genz Chat Bot ")

llm = init_chat_model(
    model="openai/gpt-oss-120b",
    model_provider="openai",
    api_key = os.getenv("groq_api"),
    base_url = "https://api.groq.com/openai/v1"
)

if "messages" not in st.session_state:
    st.session_state.messages=[
        {
            "role":"system",
            "content":"""
                You speak like a Gen-Z texter.
                Replies must be short, casual, and straight to the point.
                No long paragraphs.
                No formal grammar unless needed.
                If more detail is required, ask before explaining.        
                """
        }
    ]


for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write(msg["content"])
    elif(msg["role"]=="assistant"):
        st.markdown(msg["content"])

user=st.chat_input("Ask Anything .....")

if user :
    user_ip={
        "role":"user",
        "content":user
    }
    with st.chat_message("user"):
        st.write(user)

    st.session_state.messages.append(user_ip)

    answer=""
    box=st.empty()

    res = llm.stream(st.session_state.messages)

    for chunk in res :
        answer = answer +chunk.content
        box.markdown(answer)
    
    model_op={
        "role":"assistant",
        "content":answer
    }

    st.session_state.messages.append(model_op)