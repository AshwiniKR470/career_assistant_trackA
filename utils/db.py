import sqlite3

def init_db():
    conn = sqlite3.connect("applications.db")
    cursor = conn.cursor()
    # Applications table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            link TEXT
        )
    """)
    # Preferences table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS preferences (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT,
            location TEXT,
            experience TEXT,
            salary_min INTEGER,
            salary_max INTEGER
        )
    """)
    conn.commit()
    conn.close()

def save_preferences(pref):
    conn = sqlite3.connect("applications.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO preferences (role, location, experience, salary_min, salary_max)
        VALUES (?, ?, ?, ?, ?)
    """, (pref["role"], pref["location"], pref["experience"], pref["salary_min"], pref["salary_max"]))
    conn.commit()
    conn.close()

def get_preferences():
    conn = sqlite3.connect("applications.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM preferences ORDER BY id DESC LIMIT 1")
    pref = cursor.fetchone()
    conn.close()
    return pref
