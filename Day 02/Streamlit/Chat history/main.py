import streamlit as st
st.title("Chat model ")

if 'messages' not in st.session_state:
    st.session_state.messages = []

message = st.chat_input("Say something.....")
if message:
    st.session_state.messages.append(message)

if st.session_state.messages : 
    st.subheader("Chat History")

    for msg in st.session_state.messages:
        st.write(msg)