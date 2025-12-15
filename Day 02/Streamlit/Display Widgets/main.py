import streamlit as st
import pandas as pd
import time

#----Page Titles 
st.title("Welcome to SUNBEAM ")
st.header("This is Header")
st.subheader("This is the Subheader")

#--- st.write()
st.write("\n--------------------------------------")
st.write("st.write() :- can prints the lists,numbers,text,dicts,dataframes")
st.write("Hi")
st.write(100)
st.write([10,20,30])
st.write(
    {
        "name":"aharv",
        "age":10,
        "role":"student"
    }
)

st.write("\n--------------------------------------")

# ---- st.markdown() ----
st.markdown("""
### Markdown Output
- **Bold text**
- *Italic text*
- ` #code snippit 
    print("Hello World")`
- [Streamlit Docs](https://docs.streamlit.io)
""")

st.write("\n--------------------------------------")

# --- st.dataframe()
df = pd.DataFrame({
    "Name" : ["A" , "B" , "C"] ,
    "age":[10,20,30]
}
)
st.dataframe(df)
st.write("\n--------------------------------------\nJson Data")
#---- st.json()

data = {
    "id" : 10,
    "course" : "AI-Ml",
    "Name" : "Atharv"
}
st.json(data)

st.write("\n--------------------------------------\nToast")
#-- st.toast()
if st.button("Show Toast") :
    st.toast("This is the Temporay alert 📌")

st.write("\n--------------------------------------\nStreaming Text")
def stream_text():
    for word in ["Streaming", "text", "word", "by", "word..."]:
        yield word + " "
        time.sleep(0.7)

st.write_stream(stream_text)

# ---- st.columns() ----
col1, col2, col3 = st.columns(3)

with col1:
    st.write("Column 1")
    st.write("Name")
with col2:
    st.write("Column 2")
    st.write("Id")
with col3:
    st.write("Column 3")
    st.write("Marks")