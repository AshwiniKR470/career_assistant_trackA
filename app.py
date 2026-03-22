import streamlit as st
from scraper import scrape_jobs

st.title("AI Career Assistant - Track A")

# Step 1: Capture user input
role = st.text_input("Enter job role (e.g., Python Developer)")
location = st.text_input("Enter location", "India")

# Step 2: Use the input
if role:
    st.write(f"Searching jobs for: {role} in {location}")
    jobs = scrape_jobs(role, location)

    # Step 3: Display results
    if jobs:
        for job in jobs:
            st.markdown(f"**{job['title']}** at {job['company']}")
            st.markdown(f"[Apply Here]({job['link']})")
    else:
        st.warning("No jobs found. Try another role or location.")
experience = st.selectbox("Experience", ["Fresher", "1-3 years", "3-5 years", "5+ years"])
salary = st.text_input("Minimum Salary (e.g., 5 LPA)")