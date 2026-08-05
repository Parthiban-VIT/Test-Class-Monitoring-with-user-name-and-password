import streamlit as st
from login import login_page

st.set_page_config(
    page_title="Class Monitoring System",
    page_icon="📚",
    layout="wide"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:

    st.success(f"Welcome {st.session_state.name}")

else:

    login_page()
