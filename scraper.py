import requests

def scrape_jobs(role, location="India", experience=None, salary_min=None, salary_max=None):
    url = "https://jsearch.p.rapidapi.com/search"

    # Build query string dynamically
    query = f"{role} in {location}"
    if experience:
        query += f" {experience}"   # e.g., "junior", "mid-level", "senior"

    querystring = {"query": query, "num_pages": "1"}

    # Add salary filters if provided
    if salary_min and salary_min > 0:
        querystring["salary_min"] = str(salary_min)
    if salary_max and salary_max > 0:
        querystring["salary_max"] = str(salary_max)

    headers = {
        "X-RapidAPI-Key": "6e1dae31bdmshbc73a0e220750d1p1c1ccbjsn2580ede01379",   # 👈 paste your real key here
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code != 200:
        print("Failed to fetch jobs")
        return []

    data = response.json()
    jobs = []

    for job in data.get("data", []):
        jobs.append({
            "title": job.get("job_title"),
            "company": job.get("employer_name"),
            "link": job.get("job_apply_link")
        })

    return jobs[:10]  # return top 10 jobs