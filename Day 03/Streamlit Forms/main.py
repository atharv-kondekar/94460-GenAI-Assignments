import streamlit as st

# Registration Form 
with st.form("Reg_form"):
    st.title("Registration Form")
    fname = st.text_input("Enter your first name : ")
    lname = st.text_input("Enter your last name :")

    age = st.slider("Select your age ",10,100,22,1)

    address = st.text_area("Enter your address here ")

    btn = st.form_submit_button("Submit")

#From submission logic never written inside❌ the Form 👇🏻
if btn :
    is_error=False
    err_message=""

    if not fname  :
        is_error=True
        err_message+=" First name Can't be empty"
    
    if not lname :
        is_error=True
        err_message+="Last name Can't be empty"
    
    if not address.strip() : #Removes the White Space
        is_error=True
        err_message+="The Address is must needed"

    if is_error :
        st.error(err_message)
    else:
        message=f"Successfully Registered :{fname}{lname} Age : {age} address : {address}"
        st.success(message)