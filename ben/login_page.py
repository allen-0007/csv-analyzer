# login_page.py
import streamlit as st

def login_page():
    st.title("Allen's CSV Analyzer Login Page")
    st.markdown(
        """
        <div style="text-align: center;">
            <img src="/home/sensen/Downloads/hi.jpg" alt="WELCOME!" style="width:50%;">
        </div>
        """,
        unsafe_allow_html=True
    )
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username == "admin" and password == "123456":
            st.session_state["logged_in"] = True
            st.session_state["page"] = "main"
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

