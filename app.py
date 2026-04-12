import streamlit as st
from scraper import scrape_jobs
from utils.resume_parser import parse_resume, extract_skills
from utils.job_api import search_jobs
from utils.company_insights import get_company_info

st.title("AI Career Assistant - Track A")

# -------------------------------
# Tabs for clean separation
# -------------------------------
tab1, tab2, tab3 = st.tabs(["Resume Upload", "Job Search", "Company Insights"])

# -------------------------------
# Resume Upload Tab
# -------------------------------
with tab1:
    uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"], key="resume_uploader")
    if uploaded_file:
        resume_lines = parse_resume(uploaded_file)

        # Show point-wise resume text
        with st.expander("Extracted Resume Text (click to expand)"):
            for line in resume_lines:
                st.write(f"- {line}")

        # Join lines back into a single string for skill extraction
        resume_text = " ".join(resume_lines)
        skills = extract_skills(resume_text)

        st.subheader("Extracted Skills")
        st.write(skills)

# -------------------------------
# Job Search Tab
# -------------------------------
with tab2:
    role = st.text_input("Enter job role", "python developer")
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
    salary_min = salary_lpa_min * 100000
    salary_lpa_max = st.number_input("Maximum Salary (in LPA):", min_value=0, step=1)
    salary_max = salary_lpa_max * 100000

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

# -------------------------------
# Company Insights Tab
# -------------------------------
with tab3:
    company_name = st.text_input("Enter company name", "Infosys")
    if st.button("Get Company Info"):
        company_info = get_company_info(company_name)
        st.subheader("Company Insights")
        st.write(company_info)