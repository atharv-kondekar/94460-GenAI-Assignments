import dotenv
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
import os 

dotenv.load_dotenv()

llm = init_chat_model(
    model="llama-3.3-70b-versatile", 
    model_provider="openai",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("groq_api")
)

agent = create_agent(model=llm , tools=[])

result = agent.invoke(
    {
        "messages":[
            {
                "role":"user",
                "content":"What is the Langchain?"
            }
        ]
    }
)

print(result["messages"][-1].content)
# -1 is for the last object 
# messages :[humanmessage,aimessage]
# [-1] : aimessage[ {"role" : "...." , "content" : "...."} ]
# .cotent : is the content in the "aimessage"
