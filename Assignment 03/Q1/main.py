import streamlit as st
import pandas as pd
import pandasql as ps
import os

st.title("Query Executor")

file = st.file_uploader("Upload the CSV File ",type=['csv'])

if file is not None :
    table_name=os.path.splitext(file.name)[0]
    data=pd.read_csv(file)

    st.write("The File data")
    st.dataframe(data)

    st.markdown(f"""
    ### SQL instructions
    - table name is {table_name}
    """
    )

    query=st.text_area("Enter the SQL Query .....")
    try:
        result = ps.sqldf(query,{table_name:data})
        st.subheader("The Query Output")
        st.dataframe(result)
    except Exception as e :
        st.error(f"sql error : {e}")

else:
    st.toast("File Not Found ⚠️")



