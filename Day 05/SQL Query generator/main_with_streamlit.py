import streamlit as st
import pandas as pd 
import os
import time 
import dotenv
from langchain.chat_models import init_chat_model

st.title("QueryCraft")
dotenv.load_dotenv()

llm = init_chat_model(
    model="openai/gpt-oss-120b",
    model_provider="openai",
    api_key=os.getenv("groq_api"),
    base_url="https://api.groq.com/openai/v1"
)

# Session States
if "file" not in st.session_state:
    st.session_state.file=None

if "df" not in st.session_state:
    st.session_state.df=None

if "messages" not in st.session_state:
    st.session_state.messages=[
        {
            "role":"system",
            "content":"You are SQLite expert developer with 10 years of the experience."
        }
    ]
preview = st.container()

#Chat History 
for msg in st.session_state.messages:
    if msg["role"]=="user":
        with st.chat_message("user"):
            st.write(msg["content"])
    elif(msg["role"] == "assistant"):
        if msg["content"]=="Error":
            st.error("Unable to generate SQL for this input ")
        else:
            st.code(msg["content"],language="sql")

# File Upload Logic
if st.session_state.file is None :
    file = st.file_uploader("Upload the CSV file here ",type="csv")

    if file is not None:
        st.session_state.file=file
        st.session_state.df = pd.read_csv(file)
        st.rerun()

# Prreview  
if st.session_state.file is not None :
    with preview:
        st.success("File Uploaded Successfully ")
        df1=st.session_state.df
        st.dataframe(df1)
 

if st.session_state.file is not None:    
    df = st.session_state.df

    user = st.chat_input("Enter about this file ...")

    if user :
        st.session_state.messages.append(
            {
                "role":"user",
                "content":user
            }
        )

        llm_input=f"""
        Table_name:data
        Table Schema : {df.dtypes}
        Question:{user}
        Instruction:
             Write a SQL query for the above question. 
            Generate SQL query only SQL format and nothing else.
            If you cannot generate the query, then output 'Error'.
        """
        with st.chat_message("user"):
            st.write(user)

        answer = ""
        box=st.empty()

        res = llm.stream(llm_input)

        for chunk in res :
            answer = answer+chunk.content
            box.code(answer,language="sql")
        
        st.session_state.messages.append(
            {
                "role":"assistant",
                "content":answer
            }
        )

#else:
#   st.error("File not valid")