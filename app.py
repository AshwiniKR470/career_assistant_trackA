import streamlit as st
from scraper import scrape_jobs

st.title("AI Career Assistant - Track A")

# User inputs
role = st.text_input("Enter job role (e.g., Python Developer)", "python developer")
location = st.text_input("Enter location", "India")

# Experience mapping
experience_map = {
    "": "",
    "Fresher": "junior",
    "Mid-level": "mid-level",
    "Senior": "senior"
}
experience_choice = st.selectbox("Experience", ["", "Fresher", "Mid-level", "Senior"])
experience = experience_map[experience_choice]

# Salary input in LPA, converted to INR
salary_lpa_min = st.number_input("Minimum Salary (in LPA):", min_value=0, step=1)
salary_min = salary_lpa_min * 100000  # convert LPA → INR

salary_lpa_max = st.number_input("Maximum Salary (in LPA):", min_value=0, step=1)
salary_max = salary_lpa_max * 100000  # convert LPA → INR

# Search button
if st.button("Search Jobs"):
    st.write(f"Searching jobs for: {role} in {location}")
    jobs = scrape_jobs(role, location, experience, salary_min, salary_max)
    if jobs:
        for job in jobs:
            st.subheader(job['title'])
            st.write(f"Company: {job['company']}")
            st.markdown(f"[Apply Here]({job['link']})")
    else:
        st.warning("No jobs found. Try another role, location, or adjust filters.")