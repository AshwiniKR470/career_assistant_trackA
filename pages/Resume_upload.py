import streamlit as st
from utils.resume_parser import parse_resume, extract_skills, generate_resume_summary

st.header("Resume Upload")
resume_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])
if resume_file is not None:
    st.success("Resume uploaded successfully!")

    resume_lines = parse_resume(resume_file)
    st.subheader("Extracted Resume (Point-wise)")
    for line in resume_lines:
        st.write("• " + line)

    resume_text = "\n".join(resume_lines)
    skills = extract_skills(resume_text)

    description = generate_resume_summary(resume_lines, skills)

    st.subheader("ATS-Friendly Resume Description")
    st.write(description)

    st.subheader("Key Technologies Detected")
    st.write(", ".join(skills) if skills else "No key technologies detected.")
