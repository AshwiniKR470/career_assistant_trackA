import requests
import urllib3
from bs4 import BeautifulSoup

# Disable SSL warnings (TimesJobs cert often fails)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def fetch_timesjobs_jobs(role, location):
    """
    Fetch jobs from TimesJobs using static scraping.
    NOTE: TimesJobs is React-based, so results may be limited or empty.
    This function is kept only as a fallback.
    """
    url = (
        "https://www.timesjobs.com/candidate/job-search.html"
        f"?searchType=personalizedSearch&txtKeywords={role}&txtLocation={location}"
    )

    jobs = []
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/122.0 Safari/537.36"
        )
    }

    try:
        # ⚠️ Using verify=False to bypass SSL issues
        response = requests.get(url, headers=headers, timeout=10, verify=False)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"TimesJobs error: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    job_cards = soup.find_all("li", class_="clearfix job-bx")

    for job_card in job_cards:
        title_tag = job_card.select_one("h2 a")
        company_tag = job_card.select_one(".joblist-comp-name")
        location_tag = job_card.select_one(".top-jd-dtl span")

        if title_tag and company_tag:
            jobs.append({
                "title": title_tag.get_text(strip=True),
                "company": company_tag.get_text(strip=True),
                "location": location_tag.get_text(strip=True) if location_tag else location,
                "description": "TimesJobs listing",
                "link": title_tag["href"]
            })

    return jobs

