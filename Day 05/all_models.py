from langchain.chat_models import init_chat_model
import os 
import time 
import dotenv
import streamlit as st 

dotenv.load_dotenv()

llm = init_chat_model(
    model="openai/gpt-oss-120b",
    model_provider="openai",
    base_url = "https://api.groq.com/openai/v1",
    api_key=os.getenv("groq_api")
)

conversation = list()

while True:
    user = input("User🙋🏻: ")

    if user == "exit":
        break

    user_message={
        "role":"user",
        "content":user
    }
    conversation.append(user_message)

    answer =""
    print("Ai🤖: ")
    res = llm.stream(conversation) # we pass "conversation" here
    for chunk in res :
        answer+=chunk.content
        print(chunk.content,end="")
    
    print("\n")

    output={
        "role":"assistant",
        "content":answer
    }

    conversation.append(output)