import streamlit as st


# Streamlit session state acts like a dictionary that holds information for a single 
# user's session, & its contents are preserved between script executions

# • Critical for: Chat history, user preferences, uploaded files

#     Usage patterns:
#         • Initialize: 
#             if 'key' not in st.session_state: 
#                 st.session_state.key = value
#         • Access: 
#             st.session_state.key
#         • Update: -
#             st.session_state.key = new_value


if 'messages' not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("Settings")
    choices = ["Upper", "Lower", "Toggle"]

    # for the Selectbox
    mode = st.selectbox("Select Mode", choices)

    #for the slider
    count = st.slider("Message Count", min_value=2, max_value=10, value=6, step=2)
    
    st.subheader("Config")

    #prints the data in the json
    st.json({"mode": mode, "count": count})

#Title of your MODEL
st.title("Sunbeam Chatbot")

# Inputs the chat message
msg = st.chat_input("Say something...")

if msg:
    outmsg = msg
    if mode == "Upper":
        outmsg = msg.upper()
    elif mode == "Lower":
        outmsg = msg.lower()
    elif mode == "Toggle":
        outmsg = msg.swapcase()

    #appends the data in the list 
    st.session_state.messages.append(msg)
    st.session_state.messages.append(outmsg)

    #Access
    msglist = st.session_state.messages


    for idx, message in enumerate(msglist):
        role = "human" if idx % 2 == 0 else "ai"

        with st.chat_message(role):# Render the content as a chat bubble belonging to user or assistant.
            st.write(message)