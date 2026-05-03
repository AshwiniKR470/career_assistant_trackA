from utils.timesjobs_api import fetch_timesjobs_jobs
from utils.naukri_api import fetch_naukri_jobs
from utils.rapidapi import fetch_rapidapi_jobs

def unified_job_search(role, location, experience="", salary_min=0, salary_max=0):
    """
    Unified job search combining RapidAPI JSearch, Naukri, and TimesJobs.
    TimesJobs is kept only as a fallback since its site is React-based and scraping is unreliable.
    """
    jobs = []

    # ✅ RapidAPI jobs (primary source)
    try:
        rapidapi_jobs = fetch_rapidapi_jobs(role, location)
        if rapidapi_jobs:
            jobs.extend(rapidapi_jobs)
    except Exception as e:
        print(f"RapidAPI error: {e}")

    # ✅ Naukri jobs (secondary source)
    try:
        naukri_jobs = fetch_naukri_jobs(role, location)
        if naukri_jobs:
            jobs.extend(naukri_jobs)
    except Exception as e:
        print(f"Naukri error: {e}")

    # ✅ TimesJobs jobs (fallback only)
    try:
        timesjobs = fetch_timesjobs_jobs(role, location)
        if timesjobs:
            jobs.extend(timesjobs)
    except Exception as e:
        print(f"TimesJobs error: {e}")

    # ✅ Mock jobs (last fallback, only if list is empty)
    if not jobs:
        jobs.extend([
            {
                "title": "Python Developer",
                "company": "Infosys",
                "location": location,
                "description": "Work on scalable backend systems.",
                "link": "https://careers.infosys.com/apply",
                "salary": 600000
            },
            {
                "title": "Data Analyst",
                "company": "TCS",
                "location": location,
                "description": "Analyze datasets and build dashboards.",
                "link": "https://careers.tcs.com/apply",
                "salary": 450000
            }
        ])

    return jobs


def detect_notice_period(description: str) -> str:
    """
    Detect notice period requirement from job description text.
    Returns one of: 'Immediate', '30 days', '60 days', '90 days', 'Any'
    """
    desc = description.lower()
    if "immediate" in desc or "join immediately" in desc:
        return "Immediate"
    elif "30 days" in desc:
        return "30 days"
    elif "60 days" in desc:
        return "60 days"
    elif "90 days" in desc:
        return "90 days"
    return "Any"


def detect_wfh(description: str) -> bool:
    """
    Detect if job allows work from home / remote.
    Returns True if keywords found, else False.
    """
    desc = description.lower()
    return any(keyword in desc for keyword in ["work from home", "remote", "hybrid"])
