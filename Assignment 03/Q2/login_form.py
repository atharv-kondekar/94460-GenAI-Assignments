import pandas as pd 
import streamlit as st
import requests
import os
import json
import dotenv

dotenv.load_dotenv()

if "page" not in st.session_state:
    st.session_state.page = "login"


def loginPage():

    with st.form("login"):
        st.title("Log in Page ")
        id  = st.text_input("Enter id : .... ")
        password= st.text_input("Enetr Password.... ",type="password")

        btn  = st.form_submit_button("Log In")

    if btn : 
        if id == password and id!="":
            st.session_state.page = "weather"
        else:
            st.error("Invalid id or Password")

def weatherpage():

    st.title("Weather Page ")
    city=st.text_input("Enter the City : ")
    get=st.button("Get Weather")
    btn = st.button("log out")

    if btn:
        st.session_state.page = "thank"

    api=os.getenv("weather_api")
    url = f"https://api.openweathermap.org/data/2.5/weather?appid={api}&q={city}&units=metric"

    response = requests.get(url)
    weather=response.json()
    
    if city :
        if get:
            if response.status_code == 200:
                st.subheader(f"The Weather in {city}")
                st.write(" Temperature:", weather["main"]["temp"], "°C")
                st.write(" Humidity:", weather["main"]["humidity"], "%")
                st.write(" Wind Speed:", weather["wind"]["speed"], "m/s")
                st.write(" Condition:", weather["weather"][0]["description"])
            else:
                st.error("Enter the valid City name ")

    
def thank():
    st.title("Thank you 😊")
    st.write("Logged Out ")

if st.session_state.page == "login":
    loginPage()

elif st.session_state.page == "weather":
    weatherpage()

else:
    thank()