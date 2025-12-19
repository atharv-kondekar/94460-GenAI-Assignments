from langchain.chat_models import init_chat_model
import dotenv
import os
import time
import streamlit as st

dotenv.load_dotenv()

st.title("Clean Solver")

llm = init_chat_model(
    model="qwen/qwen3-32b",
    model_provider="openai",
    api_key = os.getenv("groq_api"),
    base_url="https://api.groq.com/openai/v1"
)

user = st.chat_input("Enter your problem : ")

if "messages" not in st.session_state:
    st.session_state.messages=[
        {
            "role" : "system",
            "content":"""Answer strictly in the required format.
            No reasoning.
            No extra explanation.
            No analysis.

            Format:
            Steps:
            1) ...
            2) ...

            Explanation:
            <max in 5-6 lines>

            Real World Analogy:
    
            Final Answer:
            <result> 
        """
        }
    ]

for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write(msg["content"])

    elif(msg["role"]=="assistant"):
        st.markdown(msg["content"])

if user :

    user_ip = {
        "role":"user",
        "content":user
    }
    st.session_state.messages.append(user_ip)

    with st.chat_message("user"):
        st.write(user)
    
    res = llm.stream(st.session_state.messages) 
    answer =""
    box=st.empty()

    for chunk in res :
        answer =answer+chunk.content
        box.markdown(answer)
    
    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )
