import streamlit as st
from utils.job_api import unified_job_search, detect_notice_period, detect_wfh
from utils.db import init_db, save_preferences, get_preferences
from utils.salary_utils import to_lpa
from utils.company_insights import analyze_company

# Initialize database
init_db()

st.header("Job Search")

# --- Input fields ---
role = st.text_input("Enter role", "Python Developer", key="role_input")
location = st.selectbox("Choose location",
                        ["Mumbai", "Bangalore", "Delhi", "Pune", "Hyderabad"],
                        key="location_select")
experience = st.selectbox("Experience Level",
                          ["Fresher", "0-2 years", "2-5 years", "5-10 years", "10+ years"],
                          key="experience_select")
salary_min = st.number_input("Minimum Salary (INR)", 0, key="salary_min_input")
salary_max = st.number_input("Maximum Salary (INR)", 0, key="salary_max_input")

# --- New filters ---
notice_period = st.selectbox("Notice Period",
                             ["Any", "Immediate", "30 days", "60 days"],
                             key="notice_period_select")
wfh_only = st.checkbox("Work From Home Only", key="wfh_checkbox")

# --- Show last search ---
last_pref = get_preferences()
if last_pref:
    st.info(f"Last search: {last_pref[1]} in {last_pref[2]} ({last_pref[3]}) "
            f"Salary {last_pref[4]}–{last_pref[5]} INR")

# --- Job Search ---
if st.button("Search Jobs", key="search_button"):
    # Save current filters
    save_preferences({
        "role": role,
        "location": location,
        "experience": experience,
        "salary_min": salary_min,
        "salary_max": salary_max
    })

    jobs = unified_job_search(role, location, experience, salary_min, salary_max)

    if jobs:
        st.subheader("Job Results")
        for job in jobs:
            # Detect attributes
            job_notice = detect_notice_period(job.get("description", ""))
            job_wfh = detect_wfh(job.get("description", ""))

            # Apply filters
            if notice_period != "Any" and job_notice != notice_period:
                continue
            if wfh_only and not job_wfh:
                continue

            # Display job
            st.write(f"**{job['title']}** at {job['company']}")
            st.write(f"📍 Location: {job.get('location', 'N/A')}")
            st.write(f"📝 Description: {job.get('description', 'No description available')}")

            # Salary in LPA
            if "salary" in job and job["salary"]:
                lpa = to_lpa(job["salary"])
                if lpa:
                    st.write(f"💰 Salary: {lpa} LPA")

            st.write(f"⏳ Notice Period: {job_notice}")
            if job_wfh:
                st.write("🏠 Work From Home available")

            # Company insights
            tags = analyze_company(job.get("description", ""))
            if tags:
                st.write("🏢 Company Insights:", ", ".join(tags))

            st.markdown(f"[Apply Here]({job['link']})")
    else:
        st.warning("No jobs found. Try another role, location, or adjust filters.")
from utils.job_api import unified_job_search, detect_notice_period, detect_wfh
