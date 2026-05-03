CULTURE_TAGS = {
    "work-life balance": ["flexible hours", "remote", "hybrid"],
    "growth": ["training", "career development", "mentorship"],
    "benefits": ["health insurance", "pf", "bonus", "perks"]
}

def analyze_company(description: str):
    """
    Scan job description text and return matching culture/benefit tags.
    """
    tags = []
    desc = description.lower()
    for category, keywords in CULTURE_TAGS.items():
        if any(keyword in desc for keyword in keywords):
            tags.append(category)
    return tags
