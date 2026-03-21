import streamlit as st

st.title("AI Career Assistant - Track A")
st.write("Welcome! This is your job search and resume helper.")

job_query = st.text_input("Enter job role (e.g., Python Developer):")

if job_query:
    st.write(f"Searching jobs for: {job_query}")
    st.success("Job results will appear here...")