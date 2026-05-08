import streamlit as st
import sqlite3
from utils.resume_parser import parse_resume, extract_skills, generate_resume_summary

st.header("Resume Upload")

# --- Upload resume ---
resume_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

if resume_file is not None:
    st.success("Resume uploaded successfully!")

    # --- Parse resume into lines ---
    resume_lines = parse_resume(resume_file)
    st.subheader("Extracted Resume (Point-wise)")
    for line in resume_lines:
        st.write("• " + line)

    # --- Convert lines to text ---
    resume_text = "\n".join(resume_lines)

    # --- Detect skills ---
    skills = extract_skills(resume_text)

    # --- Generate ATS-friendly summary ---
    description = generate_resume_summary(resume_lines, skills)

    st.subheader("ATS-Friendly Resume Description")
    st.write(description)

    st.subheader("Key Technologies Detected")
    st.write(", ".join(skills) if skills else "No key technologies detected.")

    # --- Save parsed data into SQLite ---
    # Ensure parsed_data is a dict with "content"
    parsed_data = {"content": resume_text}

    conn = sqlite3.connect("career_assistant.db")
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resumes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            content TEXT,
            skills TEXT
        )
    """)

    cursor.execute(
        "INSERT INTO resumes (filename, content, skills) VALUES (?, ?, ?)",
        (resume_file.name, parsed_data["content"], ", ".join(skills))
    )
    conn.commit()
    conn.close()
