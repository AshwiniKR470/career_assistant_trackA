import pdfplumber

def parse_resume(uploaded_file):
    """Extracts text from a PDF resume and returns it as a list of lines."""
    resume_text = ""
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                resume_text += text + "\n"
    lines = [line.strip() for line in resume_text.split("\n") if line.strip()]
    return lines

def extract_skills(resume_text: str):
    """Extracts known skills from resume text by matching against a predefined list."""
    skills_list = [
        "Python", "Java", "C++", "JavaScript", "SQL", "MySQL", "PostgreSQL",
        "MongoDB", "Streamlit", "Flask", "Django", "React", "Node.js",
        "TensorFlow", "PyTorch", "Keras", "Scikit-learn", "AWS", "Azure",
        "Google Cloud", "Docker", "Kubernetes", "Git", "GitHub"
    ]
    found_skills = [skill for skill in skills_list if skill.lower() in resume_text.lower()]
    return found_skills

def generate_resume_summary(resume_lines, skills):
    """Generate ATS-friendly description based on parsed resume lines and detected skills."""
    description = (
        "Full Stack Developer with proven expertise in building scalable, modular applications. "
        "Strong background in algorithmic problem-solving, API integration, and cloud deployment. "
        "Experienced in maintaining professional repo hygiene and translating technical workflows "
        "into accessible documentation."
    )
    if skills:
        description += " Key technologies include: " + ", ".join(skills) + "."
    return description
