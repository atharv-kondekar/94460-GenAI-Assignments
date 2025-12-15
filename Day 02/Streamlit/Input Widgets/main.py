import streamlit as st
import pandas as pd

st.title("Streamlit Input Widgets Demo ")

#Text input single line 
name  = st.text_input("Enter your name : ")

#Text input multi-line 
query = st.text_area("Enter the Query : ")

#File Uploader 
file_uploader = st.file_uploader("Upload the CSV File ... ",type=["csv"])

#Dropdown-box
role = st.selectbox("Select your role",["Student","Developer","Engineer","Other"])

#slider
age = st.slider("Select your CGPA : ",min_value=0,max_value=10,value=6,step=2)

if st.button("Submit"):
    st.subheader("Submitted Data ")

    st.write("Name : ",name)
    st.write("Query : ",query)
    st.write("Role : ",role)
    st.write("Age : ",age)

    if file_uploader is not None:
        df=pd.read_csv(file_uploader)
        st.write("Uploaded file data : ")
        st.dataframe(df)
    else:
        st.write("No File uploaded ... ")
