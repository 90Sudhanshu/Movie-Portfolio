import streamlit as st

st.header("Contact Us..!!!")

with st.form(key="my form"):
    st.text_input("Enter your mail", placeholder="Enter e-mail only")
    st.text_area("Enter your query", placeholder="Enter in brief")
    st.form_submit_button("Send")
