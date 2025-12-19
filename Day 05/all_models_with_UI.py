import streamlit as st
import os
import time
import dotenv
from langchain.chat_models import init_chat_model

dotenv.load_dotenv()
st.title("Chat Bot with Chat Memory ")
if "messages" not in st.session_state:
    st.session_state.messages=[]

#just make changes here
llm = init_chat_model(
    model="openai/gpt-oss-120b", 
    model_provider="openai",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("groq_api")
)

for msg in st.session_state.messages:
    if msg["role"]=="user":
        with st.chat_message("user"):
            st.write(msg["content"])
    else:
        st.markdown(msg["content"])

# ***********
# ❌ Here there is the NO use of the "Conversation list "
# conversation = list() #NO use

user=st.chat_input("Ask anything ....")

if user :
    
    userip = {
        "role" : "user",
        "content":user
    }
  # conversation.append(userip)
    st.session_state.messages.append(userip)
    with st.chat_message("user"):
        st.write(user)


    # ✅ We have to pass here  "st.session_state.messages"
    res=llm.stream(st.session_state.messages)

    box = st.empty()
    answer=""
    for chunk in res:
        answer+=chunk.content
        time.sleep(0.01)
        box.markdown(answer)
    
    llm_op = {
        "role":"assistant",
        "content":answer
    }

    #conversation.append(llm_op)
    st.session_state.messages.append(llm_op)
