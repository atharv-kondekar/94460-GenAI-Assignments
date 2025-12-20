import pandas as pd
from langchain.chat_models import init_chat_model
import os 
import dotenv 

dotenv.load_dotenv()

llm=init_chat_model(
    model="openai/gpt-oss-120b",
    model_provider="openai",
    api_key=os.getenv("groq_api"),
    base_url="https://api.groq.com/openai/v1"
)

conversation = [
    {
        "role" : "system",
        "content":"You are SQLite expert developer with 10 years of the experience."
    }
]

csv_file= input("Enter CSV File Path : ")
df= pd.read_csv(csv_file)
schemas = df.dtypes
print(schemas)

while True :
    user = input("Ask Anything about this file : ")

    if user =="exit":
        break

    llm_input=f"""
        Table_name:data
        Table Schema : {df.dtypes}
        Question:{user}
        Instruction:
             Write a SQL query for the above question. 
            Generate SQL query only SQL format and nothing else.
            If you cannot generate the query, then output 'Error'.
    """

    res = llm.invoke(llm_input)
    print(res.content)