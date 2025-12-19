import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import dotenv
import os

dotenv.load_dotenv()

st.header("Your Chatbot")

api = os.getenv("groq_api")

if "messages" not in st.session_state:
    st.session_state.messages = []

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=api,
    streaming=True
)

# show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

ip = st.chat_input("Ask anything...")

if ip:

    st.session_state.messages.append(
        {
            "role": "user", 
            "content": ip
        }
    )

    with st.chat_message("user"):
        st.write(ip)

    
    with st.chat_message("assistant"):
        answer = ""
        box = st.empty() #It creates the one ui slot 

        stream = llm.stream([HumanMessage(content=ip)])
        for chunk in stream:
            if chunk.content:
                answer += chunk.content
                box.markdown(answer) #overwrites that slot each time 
    
    st.session_state.messages.append(
        {
            "role": "assistant", 
            "content": answer
        }
    )
