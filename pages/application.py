import sqlite3
import streamlit as st
import sys, os
from fpdf import FPDF
from fpdf.enums import XPos, YPos

# Add parent folder to path so "utils" can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.job_api import fetch_naukri_jobs
from utils.timesjobs_api import fetch_timesjobs_jobs

# --- Load applications from DB ---
def load_applications():
    conn = sqlite3.connect("applications.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, company, location, link FROM applications")
    rows = cursor.fetchall()
    conn.close()
    return rows

# --- Export jobs to PDF ---
def export_jobs(rows):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)
    pdf.cell(200, 10, "Job Applications", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Add table headers
    pdf.set_font("Helvetica", size=11)
    pdf.cell(60, 10, "Job Title", border=1)
    pdf.cell(60, 10, "Company", border=1)
    pdf.cell(60, 10, "Location", border=1)
    pdf.cell(60, 10, "Apply Link", border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Add rows
    for job in rows:
        pdf.cell(60, 10, job[1], border=1)
        pdf.cell(60, 10, job[2], border=1)
        pdf.cell(60, 10, job[3], border=1)
        pdf.cell(60, 10, job[4], border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # ✅ Convert bytearray → bytes explicitly
    pdf_bytes = pdf.output(dest="S")
    if isinstance(pdf_bytes, bytearray):
        pdf_bytes = bytes(pdf_bytes)
    return pdf_bytes

# --- Main UI ---
rows = load_applications()
st.title("Job Applications Tracker")

# --- Display saved applications ---
if rows:
    st.subheader("Saved Applications")
    for id, title, company, location, link in rows:
        col1, col2, col3 = st.columns([2, 2, 2])
        col1.write(f"**{title}**")
        col2.write(company)
        col3.write(location)
        st.markdown(f"[Apply Here]({link})")

    # ✅ PDF download button AFTER export_jobs is defined
    try:
        pdf_bytes = export_jobs(rows)
        st.download_button(
            label="📄 Download Job List PDF",
            data=pdf_bytes,
            file_name="jobs.pdf",
            mime="application/pdf"
        )
    except Exception as e:
        st.error(f"PDF export failed: {e}")
else:
    st.info("No saved applications yet.")

# --- API fallback example ---
st.subheader("Sample Job Listings")

role = st.text_input("Job Role", "Python Developer")
location = st.text_input("Location", "Mumbai")

jobs = []
try:
    jobs = fetch_naukri_jobs(role, location)
except Exception:
    st.warning("Naukri API failed, switching to TimesJobs...")
    try:
        jobs = fetch_timesjobs_jobs(role, location)
    except Exception:
        st.error("Both Naukri and TimesJobs APIs failed.")

# ✅ Fallback mock jobs if APIs return empty
if not jobs:
    jobs = [
        {"title": "Python Developer", "company": "Infosys", "location": "Bangalore", "link": "https://example.com/apply1"},
        {"title": "Data Analyst", "company": "TCS", "location": "Mumbai", "link": "https://example.com/apply2"},
        {"title": "Frontend Engineer", "company": "Wipro", "location": "Hyderabad", "link": "https://example.com/apply3"},
    ]

if jobs:
    for job in jobs:
        st.write(f"**{job['title']}** at {job['company']} ({job.get('location', 'N/A')})")
        st.markdown(f"[Apply Here]({job['link']})")
else:
    st.info("No sample job listings available.")
