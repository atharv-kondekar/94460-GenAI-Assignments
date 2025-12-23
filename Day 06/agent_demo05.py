from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

while True:
    user = input("Human : ")
    response = client.chat.completions.create(
        model="meta-llama-3.1-8b-instruct",
        messages=[
            {"role": "user", "content": user}
        ],
        max_tokens=100
    )

    print(response.choices[0].message.content)