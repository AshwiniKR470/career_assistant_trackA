import streamlit as st

company_data = {
    "Infosys": {
        "Culture": "Collaborative, innovation-driven, emphasis on learning",
        "Benefits": ["Health Insurance", "Work From Home Policy", "Training Programs"],
        "Policies": ["Flexible working hours", "Employee wellness programs"]
    },
    "TCS": {
        "Culture": "Process-oriented, stability-focused, strong client relationships",
        "Benefits": ["Medical Insurance", "Retirement Plans", "Onsite Opportunities"],
        "Policies": ["Strict project timelines", "Structured career growth"]
    },
    "Wipro": {
        "Culture": "Customer-centric, diverse workforce, innovation focus",
        "Benefits": ["Health Insurance", "Paid Leave", "Skill Development"],
        "Policies": ["Hybrid work model", "Employee engagement programs"]
    }
}

st.header("Company Insights")

company_name = st.selectbox("Select a company", list(company_data.keys()), key="company_select")

if company_name:
    info = company_data[company_name]
    st.subheader(company_name)
    st.write(f"**Culture:** {info['Culture']}")
    st.write("**Benefits:**")
    for benefit in info["Benefits"]:
        st.write(f"- {benefit}")
    st.write("**Policies:**")
    for policy in info["Policies"]:
        st.write(f"- {policy}")
import streamlit as st
from utils.company_insights import analyze_company

st.header("Company Insights")

company = st.selectbox("Select a company", ["Infosys", "TCS", "Wipro", "Accenture"])

# Static info (example)
if company == "Infosys":
    st.write("Culture: Collaborative, innovation-driven")
    st.write("Benefits: Health insurance, PF, flexible hours")

# Keyword analysis (optional demo)
desc = st.text_area("Paste a job description to analyze")
if desc:
    tags = analyze_company(desc)
    if tags:
        st.success(f"Detected culture/benefits: {', '.join(tags)}")
    else:
        st.warning("No culture/benefits keywords detected.")
