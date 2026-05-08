import sqlite3

# -----------------------------
# Resume Table (career_assistant.db)
# -----------------------------
def init_resume_db():
    """Initialize the resumes table in career_assistant.db"""
    conn = sqlite3.connect("career_assistant.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resumes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            content TEXT,
            skills TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_resume(filename, content, skills):
    """Save a parsed resume into the resumes table"""
    conn = sqlite3.connect("career_assistant.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO resumes (filename, content, skills) VALUES (?, ?, ?)",
        (filename, content, skills)
    )
    conn.commit()
    conn.close()

def get_resumes():
    """Retrieve all saved resumes"""
    conn = sqlite3.connect("career_assistant.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM resumes")
    rows = cursor.fetchall()
    conn.close()
    return rows


# -----------------------------
# Applications Table (applications.db)
# -----------------------------
def init_applications_db():
    """Initialize the applications table in applications.db"""
    conn = sqlite3.connect("applications.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            link TEXT,
            status TEXT DEFAULT 'Applied'
        )
    """)
    conn.commit()
    conn.close()

def save_application(title, company, location, link, status="Applied"):
    """Save a job application into the applications table"""
    conn = sqlite3.connect("applications.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO applications (title, company, location, link, status) VALUES (?, ?, ?, ?, ?)",
        (title, company, location, link, status)
    )
    conn.commit()
    conn.close()

def get_applications():
    """Retrieve all saved job applications"""
    conn = sqlite3.connect("applications.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM applications")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_application_status(app_id, new_status):
    """Update the status of a job application"""
    conn = sqlite3.connect("applications.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE applications SET status=? WHERE id=?",
        (new_status, app_id)
    )
    conn.commit()
    conn.close()


# -----------------------------
# Preferences Table (applications.db)
# -----------------------------
def init_preferences_db():
    """Initialize the preferences table in applications.db"""
    conn = sqlite3.connect("applications.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS preferences (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT,
            location TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_preferences(role, location):
    """Save user job search preferences"""
    conn = sqlite3.connect("applications.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO preferences (role, location) VALUES (?, ?)", (role, location))
    conn.commit()
    conn.close()

def get_preferences():
    """Retrieve the most recent job search preferences"""
    conn = sqlite3.connect("applications.db")
    cursor = conn.cursor()
    cursor.execute("SELECT role, location FROM preferences ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    return row if row else ("Python Developer", "Mumbai")
