from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool 
import os
import dotenv

dotenv.load_dotenv()

@tool
def calculator(expression : str )->str:
    """
    This is the calculator function that solves any arithmetic expression for all constant values.
    It supports basic arithmetic operators +,-,*,/, and parenthesis
    
    :param expression: str input arithmetic expression
    :return: expression result as string
    """

    try:
        result  = eval(expression)
        return str(result)
    except:
        return "Cannot Solve the Problem"

@tool
def read_file(filename : str)->str:
    """
    Reads and returns the contents of a text file.
    Filename should be relative to the current working directory.
    Example: read_file("data.txt")
    """

    try:
        if not os.path.exists(filename):
            return f"Error {filename} not exists"
        with open(filename,'r') as f :
            content = f.read()
        return content
    
    except Exception as e : 
        return f"Error Reading file : {str (e) }"

llm = init_chat_model(
    model="llama-3.3-70b-versatile",
    model_provider="openai",
    api_key=os.getenv("groq_api"),
    base_url="http://127.0.0.1:1234/v1"
)
 
agent=create_agent(
    model=llm,
    tools=[read_file,calculator],
    system_prompt="""
        You are a tool-using assistant.

        Rules:
        - If the user gives a filename, call read_file with the EXACT same filename.
        - Do NOT modify, shorten, or guess filenames.
        - Use calculator ONLY for arithmetic expressions.
        - If a file does not exist, return the error from the tool.
        """
)

while True:
    user = input("Enter the file path : ")

    if user == "exit":
        break 

    result = agent.invoke(
        {
            "messages":[
                {
                    "role":"user",
                    "content":f"Read EXACTLY this file and do not change the filename: {user}"
                }
            ]
        }
    )

    output = result["messages"][-1]
    print("AI 🤖 : ",output.content)