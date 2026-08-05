import streamlit as st
from login import login_page

st.set_page_config(
    page_title="Class Monitoring System",
    page_icon="📚",
    layout="centered"
)

login_page()
