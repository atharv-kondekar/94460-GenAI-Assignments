from langchain_groq import ChatGroq
import os 
import dotenv

dotenv.load_dotenv()

api = os.getenv("groq_api")
grq_llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=api
)

while True:
    user = input("Human🙋🏻 : ")

    if user =="exit":
        break

    res = grq_llm.stream(user)
    print("Ai🤖:")
    for chunk in res :
        print(chunk.content,end="")
    print("\n")