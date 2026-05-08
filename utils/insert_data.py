import sqlite3

def insert_20_applications():
    conn = sqlite3.connect("applications.db")
    cursor = conn.cursor()

    sample_data = [
        ("Python Developer", "Infosys", "Bangalore", "https://naukri.com/job/123"),
        ("Data Analyst", "TCS", "Mumbai", "https://timesjobs.com/job/456"),
        ("Frontend Engineer", "Wipro", "Hyderabad", "https://linkedin.com/job/789"),
        ("ML Engineer", "Google", "Bangalore", "https://careers.google.com/job/111"),
        ("Cloud Architect", "AWS", "Hyderabad", "https://aws.amazon.com/job/222"),
        ("DevOps Engineer", "Microsoft", "Bangalore", "https://careers.microsoft.com/job/333"),
        ("Backend Developer", "Flipkart", "Delhi", "https://flipkart.com/job/444"),
        ("AI Researcher", "OpenAI", "Remote", "https://openai.com/job/555"),
        ("Cybersecurity Analyst", "Cisco", "Pune", "https://cisco.com/job/666"),
        ("UI/UX Designer", "Adobe", "Noida", "https://adobe.com/job/777"),
        ("Blockchain Developer", "Polygon", "Remote", "https://polygon.technology/job/888"),
        ("Game Developer", "Ubisoft", "Pune", "https://ubisoft.com/job/999"),
        ("Mobile Developer", "Samsung", "Chennai", "https://samsung.com/job/1010"),
        ("Data Scientist", "IBM", "Bangalore", "https://ibm.com/job/1111"),
        ("AI Engineer", "NVIDIA", "Pune", "https://nvidia.com/job/1212"),
        ("Software Engineer", "Oracle", "Hyderabad", "https://oracle.com/job/1313"),
        ("Product Manager", "Meta", "Remote", "https://meta.com/job/1414"),
        ("QA Engineer", "Accenture", "Delhi", "https://accenture.com/job/1515"),
        ("Systems Engineer", "HCL", "Chennai", "https://hcl.com/job/1616"),
        ("Full Stack Developer", "Capgemini", "Bangalore", "https://capgemini.com/job/1717")
    ]

    cursor.executemany("""
        INSERT INTO applications (title, company, location, link)
        VALUES (?, ?, ?, ?)
    """, sample_data)

    conn.commit()
    conn.close()
    

if __name__ == "__main__":
    insert_20_applications()
