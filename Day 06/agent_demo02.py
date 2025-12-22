import os 
import dotenv

from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool
dotenv.load_dotenv()

llm = init_chat_model(
    model="llama-3.3-70b-versatile",
    model_provider="openai",
    api_key=os.getenv("groq_api"),
    base_url="https://api.groq.com/openai/v1"
)

@tool
def calculator(expression:str)->str:
    """
    This is the calculator function that solves any arithmetic expression for all constant values.
    It supports basic arithmetic operators +,-,*,/, and parenthesis
    
    :param expression: str input arithmetic expression
    :return: expression result as string
    """

    try:
        result = eval(expression)
        return str(result)
    except:
        return "Error : Connot solve expression"


agent = create_agent(
        model=llm,
        tools=[calculator],
        system_prompt="You are the helpful assistant . Answer in short"
    )

while True : 
    user = input("You : ")

    if user == "exit":
        break

    result = agent.invoke(
        {
            "messages":[
                {
                    "role":"user",
                    "content":user
                }
            ]
        }
    )

    llm_output = result["messages"][-1]

    print("Ai Message 🤖: ",llm_output.content)