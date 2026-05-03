import requests
from bs4 import BeautifulSoup

def fetch_naukri_jobs(role, location):
    jobs = []
    try:
        url = f"https://www.naukri.com/{role}-jobs-in-{location}"
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, "html.parser")

        listings = soup.find_all("article", class_="jobTuple")
        for listing in listings[:5]:  # limit to 5 jobs
            title = listing.find("a", class_="title").text.strip()
            company = listing.find("a", class_="subTitle").text.strip()
            link = listing.find("a", class_="title")["href"]
            desc = listing.find("div", class_="job-description").text.strip() if listing.find("div", class_="job-description") else ""
            jobs.append({
                "title": title,
                "company": company,
                "location": location,
                "description": desc,
                "link": link,
                "salary": None
            })
    except Exception as e:
        print(f"Naukri scrape error: {e}")
    return jobs
