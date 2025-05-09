# app.py

import streamlit as st
from agent import run_agent 

st.set_page_config(page_title="AI Task Agent (Gemini)", layout="wide")

st.title("🤖 AI Task Agent using Google Gemini")
st.markdown("Ask any question and get a smart response using Gemini API.")

user_input = st.text_input("Enter your task or question:")

if st.button("Run Agent") and user_input:
    with st.spinner("Thinking..."):
        response = run_agent(user_input)
        st.success("Done!")
        st.markdown("### Agent Response:")
        st.write(response)
