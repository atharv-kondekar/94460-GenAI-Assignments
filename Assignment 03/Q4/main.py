
import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="CSV Portal", layout="wide")

USERS_FILE = "users.csv"
HISTORY_FILE = "userfiles.csv"

# ---------------- SESSION STATE ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.userid = None

# ---------------- HELPERS ----------------
def load_users():
    return pd.read_csv(USERS_FILE)

def save_history(userid, filename):
    new_row = pd.DataFrame([{
        "userid": userid,
        "filename": filename,
        "uploaded_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }])

    if os.path.exists(HISTORY_FILE):
        df = pd.read_csv(HISTORY_FILE)
        df = pd.concat([df, new_row], ignore_index=True)
    else:
        df = new_row

    df.to_csv(HISTORY_FILE, index=False)

# ---------------- SIDEBAR MENU ----------------
st.sidebar.title("Menu")

if not st.session_state.logged_in:
    menu = st.sidebar.radio(
        "Navigation",
        ["Home", "Login", "Register"]
    )
else:
    menu = st.sidebar.radio(
        f"Welcome, {st.session_state.userid}",
        ["Explore CSV", "See History", "Logout"]
    )

# ---------------- UNAUTHENTICATED PAGES ----------------
if not st.session_state.logged_in:

    if menu == "Home":
        st.title("Home")
        st.write("Please login or register to continue.")

    elif menu == "Login":
        st.title("Login")

        userid = st.text_input("User ID")
        password = st.text_input("Password", type="password")
        login_btn = st.button("Login")

        if login_btn:
            users = load_users()
            valid = users[
                (users["userid"] == userid) &
                (users["password"] == password)
            ]

            if not valid.empty:
                st.session_state.logged_in = True
                st.session_state.userid = userid
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Invalid credentials")

    elif menu == "Register":
        st.title("Register")

        new_user = st.text_input("New User ID")
        new_pass = st.text_input("New Password", type="password")
        reg_btn = st.button("Register")

        if reg_btn:
            users = load_users()

            if new_user in users["userid"].values:
                st.error("User already exists")
            elif new_user == "" or new_pass == "":
                st.error("Fields cannot be empty")
            else:
                users.loc[len(users)] = [new_user, new_pass]
                users.to_csv(USERS_FILE, index=False)
                st.success("Registration successful")

# ---------------- AUTHENTICATED PAGES ----------------
else:

    if menu == "Explore CSV":
        st.title("Upload & Explore CSV")

        uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

        if uploaded_file:
            df = pd.read_csv(uploaded_file)
            st.dataframe(df)

            save_history(
                st.session_state.userid,
                uploaded_file.name
            )

            st.success("File uploaded and history saved")

    elif menu == "See History":
        st.title("Upload History")

        if os.path.exists(HISTORY_FILE):
            history = pd.read_csv(HISTORY_FILE)
            user_history = history[
                history["userid"] == st.session_state.userid
            ]

            if user_history.empty:
                st.info("No uploads yet")
            else:
                st.dataframe(user_history)
        else:
            st.info("No history file found")

    elif menu == "Logout":
        st.session_state.logged_in = False
        st.session_state.userid = None
        st.success("Logged out")
        st.rerun()
