import streamlit as st
import requests
import dotenv
import json
import os

# ---------- ENV ----------
dotenv.load_dotenv()

GROQ_API = os.getenv("groq_api")

CLOUD_URL = "https://api.groq.com/openai/v1/chat/completions"
LOCAL_URL = "http://127.0.0.1:1234/v1/chat/completions"

CLOUD_HEADERS = {
    "Authorization": f"Bearer {GROQ_API}",
    "Content-Type": "application/json"
}

LOCAL_HEADERS = {
    "Authorization": "Bearer dummy",
    "Content-Type": "application/json"
}

# ---------- SESSION STATE ----------
if "cloud_messages" not in st.session_state:
    st.session_state.cloud_messages = []

if "local_messages" not in st.session_state:
    st.session_state.local_messages = []

# ---------- UI ----------
st.title("Multiple Chatbots")

with st.sidebar:
    st.header("Switch API")
    mode = st.selectbox(
        "Select Model",
        ["Local API", "Cloud Based API"]
    )

# Choose correct memory
messages = (
    st.session_state.cloud_messages
    if mode == "Cloud Based API"
    else st.session_state.local_messages
)

# Render chat history
for msg in messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ---------- CHAT INPUT ----------
user_input = st.chat_input("Ask Anything...")

if user_input:
    # Store user message
    messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    payload = {
        "model": (
            "llama-3.3-70b-versatile"
            if mode == "Cloud Based API"
            else "meta-llama-3.1-8b-instruct"
        ),
        "messages": messages
    }

    response = requests.post(
        CLOUD_URL if mode == "Cloud Based API" else LOCAL_URL,
        headers=CLOUD_HEADERS if mode == "Cloud Based API" else LOCAL_HEADERS,
        json=payload,
        timeout=60
    )

    if response.status_code != 200:
        st.error(f"HTTP Error {response.status_code}")
        st.code(response.text)
    else:
        data = response.json()

        if "choices" not in data:
            st.error("Invalid API Response")
            st.json(data)
        else:
            ai_reply = data["choices"][0]["message"]["content"]

            messages.append(
                {"role": "assistant", "content": ai_reply}
            )

            with st.chat_message("assistant"):
                st.write(ai_reply)

