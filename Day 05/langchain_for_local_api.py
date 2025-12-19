from langchain_openai import ChatOpenAI

url = "http://127.0.0.1:1234/v1"

llm = ChatOpenAI(
    model="meta-llama-3.1-8b-instruct",
    api_key="dummy",
    base_url=url
)

while True:
    user = input("Human🙋🏻 : ")

    if user =="exit":
        break

    res = llm.invoke(user)
    print("Ai🤖: ",res.content)
