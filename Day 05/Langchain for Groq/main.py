from langchain_groq import ChatGroq
import dotenv
import os
dotenv.load_dotenv()

api = os.getenv("groq_api")

llm = ChatGroq(model="openai/gpt-oss-120b",api_key=api)

while True :
    user = input("Human🙋🏻  : ")
    if user == "exit":
        break

    result = llm.invoke(user)

    print("Ai🤖 : ",result.content)

print("Thank You :) ")