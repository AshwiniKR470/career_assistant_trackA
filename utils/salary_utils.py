def to_lpa(salary_in_inr):
    """
    Convert salary in INR to Lakhs Per Annum (LPA).
    Example: 600000 INR -> 6.0 LPA
    """
    if not salary_in_inr or salary_in_inr <= 0:
        return None
    return round(salary_in_inr / 100000, 2)
