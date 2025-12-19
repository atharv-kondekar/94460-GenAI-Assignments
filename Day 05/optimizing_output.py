from langchain.chat_models import init_chat_model
import os
import time 
import dotenv

dotenv.load_dotenv()

llm = init_chat_model(
    model="openai/gpt-oss-120b",
    model_provider="openai",
    api_key = os.getenv("groq_api"),
    base_url="https://api.groq.com/openai/v1"
)

conversation = [
    {
        "role":"system" ,
        "content":"You speak in casual GenZ slang. Keep replies short, witty, and informal."
    }
]

while True : 
    user =input("Ask Anything: ") 

    if user == "exit":
        break

    user_ip ={
        "role":"user", 
        "content":user
    }

    conversation.append(user_ip)

    answer=""
    res = llm.stream(conversation)
    for chunk in res:
        print(chunk.content,end="")
        time.sleep(0.01)
        answer+=chunk.content
    
    system_op={
        "role":"system",
        "content":answer
    }