import requests

def search_jobs(role, location, experience=None, salary_min=None, salary_max=None):
    url = "https://jsearch.p.rapidapi.com/search"
    query = f"{role} in {location}"
    if experience:
        query += f" {experience}"

    querystring = {"query": query, "num_pages": "1"}
    if salary_min: querystring["salary_min"] = str(salary_min)
    if salary_max: querystring["salary_max"] = str(salary_max)

    headers = {"X-RapidAPI-Key": "6e1dae31bdmshbc73a0e220750d1p1c1ccbjsn2580ede01379"}
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()