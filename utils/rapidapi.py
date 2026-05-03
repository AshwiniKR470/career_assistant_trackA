import requests

API_HOST = "jsearch.p.rapidapi.com"
API_KEY = "6e1dae31bdmshbc73a0e220750d1p1c1ccbjsn2580ede01379"  # replace with your key

def fetch_rapidapi_jobs(role, location):
    jobs = []
    try:
        url = f"https://{API_HOST}/search"
        querystring = {"query": f"{role} in {location}", "num_pages": "1"}
        headers = {
            "X-RapidAPI-Key": API_KEY,
            "X-RapidAPI-Host": API_HOST
        }
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()

        for item in data.get("data", [])[:5]:  # limit to 5 jobs
            jobs.append({
                "title": item.get("job_title"),
                "company": item.get("employer_name"),
                "location": item.get("job_city"),
                "description": item.get("job_description"),
                "link": item.get("job_apply_link"),
                "salary": None
            })
    except Exception as e:
        print(f"RapidAPI error: {e}")
    return jobs
