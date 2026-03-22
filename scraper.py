import requests
from bs4 import BeautifulSoup

def scrape_jobs(role, location="India"):
    """
    Scrape job listings from Naukri based on role and location.
    Returns a list of dictionaries with title, company, and link.
    """

    # Build search URL dynamically
    role = role.replace(" ", "-")  # convert spaces to hyphens
    location = location.replace(" ", "-")
    url = f"https://www.naukri.com/{role}-jobs-in-{location}"

    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    if response.status_code != 200:
        print("Failed to fetch jobs")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []
    for job_card in soup.select(".jobTuple"):
        title_tag = job_card.select_one(".title")
        company_tag = job_card.select_one(".subTitle")

        if title_tag and company_tag:
            title = title_tag.get_text(strip=True)
            company = company_tag.get_text(strip=True)
            link = title_tag.find("a")["href"]

            jobs.append({
                "title": title,
                "company": company,
                "link": link
            })

    return jobs[:10]  # Limit to 10 results


# -------------------------
# Quick test when run directly
# -------------------------
if __name__ == "__main__":
    test_jobs = scrape_jobs("python-developer", "bangalore")
    for job in test_jobs:
        print(f"{job['title']} at {job['company']}")
        print(f"Apply: {job['link']}\n")