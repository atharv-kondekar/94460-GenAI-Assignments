from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool
from dotenv import load_dotenv
import os

load_dotenv()

#TOOLS
@tool
def read_file(filepath: str) -> str:
    """
    Reads and returns the contents of a local file.
    The filepath must be used exactly as provided.
    """
    try:
        if not os.path.exists(filepath):
            return f"Error: {filepath} does not exist"

        with open(filepath, "r") as f:
            return f.read()

    except Exception as e:
        return f"Error reading file: {str(e)}"


@tool
def calculator(expression: str) -> str:
    """
    This calculator function solves any arithmetic expression containing all constant values.
    It supports basic arithmetic operators +, -, *, /, and parenthesis. 
    
    :param expression: str input arithmetic expression
    :returns expression result as str
    """
    try:
        return str(eval(expression))
    except Exception:
        return "Error: Cannot evaluate expression"


#LLM
llm = init_chat_model(
    model="meta-llama-3.1-8b-instruct",   
    model_provider="openai",
    base_url="http://127.0.0.1:1234/v1",
    api_key="dummy"
)

#AGENT
agent = create_agent(
    model=llm,
    tools=[read_file, calculator],
    system_prompt="""
You are a STRICT tool-using assistant.

RULES (NO EXCEPTIONS):
- If the user input ends with .txt, .csv, or .json,
  you MUST call the read_file tool with the EXACT same filename.
- Do NOT explain anything.
- Do NOT ask questions.
- Just return the file contents.
"""
)

#LOOP 
while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        break

    result = agent.invoke({
            "messages":[
                {
                    "role":"user",
                    "content":user_input
                }
            ]
        })

    output = result["messages"][-1]
    print("\nAI:\n")
    print(output.content)
    print("-" * 50)
