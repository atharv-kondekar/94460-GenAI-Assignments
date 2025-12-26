# Create a Streamlit application that takes a city name as input from the user.
# Fetch the current weather using a Weather API and use an LLM to explain the weather conditions in simple English.

import os 
import dotenv
from langchain.chat_models import init_chat_model
import requests



dotenv.load_dotenv()

llm = init_chat_model(
    model="openai/gpt-oss-120b",
    model_provider="openai",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("groq_api")
)

weather_api = os.getenv("open_weather")
System_message =f""" You interpret live weather data and explain it in simple, clear English.
Rules:
- Do not invent data.
- No exaggeration or dramatic language.
- 3 to 5 sentences max.
- Make the explanation practical (umbrella, clothing, outdoor suitability).
- If data is missing or invalid, say so directly.
"""

while True:
    user = input("\n Enter the City name : ")

    if user.lower() == "exit":
        break

    url = f"https://api.openweathermap.org/data/2.5/weather?q={user}&appid={weather_api}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error : City not found ")
        continue

    data =response.json()

    temp=data['main']['temp']
    desc=data['weather'][0]['description']
    humidity=data['main']['humidity']
    wind = data['wind']['speed']

    llm_input= f"""
    City :{user}
    Tenpeature : {temp}°C
    Condition:{desc}
    Humidity:{humidity}%
    Wind speed:{wind}m/s
    """

    result = llm.stream(
        [
            {
                "role":"system" ,
                "content":System_message
            },

            {
                "role":"user",
                "content":llm_input
            }
        ]
    )

    print(f"------The Weather Condition in {user}--------")
    for chunk in result:
        print(chunk.content,end="")