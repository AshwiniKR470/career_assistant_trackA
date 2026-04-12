import pdfplumber

def parse_resume(uploaded_file):
    """
    Extracts text from a PDF resume and returns it as a list of lines
    for point-wise readability.
    """
    resume_text = ""
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                resume_text += text + "\n"

    # Split into clean lines
    lines = [line.strip() for line in resume_text.split("\n") if line.strip()]
    return lines


def extract_skills(resume_text: str):
    """
    Extracts known skills from resume text by matching against a predefined list.
    """
    skills_list = [
        # Programming Languages
        "Python", "Java", "C++", "C", "C#", "JavaScript", "TypeScript", "Go", "Rust", "Ruby", "PHP",
        # Databases
        "SQL", "MySQL", "PostgreSQL", "MongoDB", "SQLite", "Oracle",
        # Web Development
        "HTML", "CSS", "React", "Angular", "Vue.js", "Django", "Flask", "Spring Boot", "Node.js", "Express",
        # AI / ML
        "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch", "Keras", "Scikit-learn", "NLP",
        "Computer Vision", "Agentic AI",
        # Data / Analytics
        "Data Analysis", "Pandas", "NumPy", "Matplotlib", "Seaborn", "Power BI", "Tableau",
        # Cloud / DevOps
        "AWS", "Azure", "Google Cloud", "Docker", "Kubernetes", "CI/CD", "Git", "GitHub",
        # Other Tools
        "Excel", "Jupyter Notebook", "VS Code", "IntelliJ", "Eclipse"
    ]

    found_skills = [skill for skill in skills_list if skill.lower() in resume_text.lower()]
    return found_skills