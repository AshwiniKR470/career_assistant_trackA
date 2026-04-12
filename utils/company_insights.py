import requests

def get_company_info(company_name):
    url = "https://company-clearbit.p.rapidapi.com/v2/companies/find"
    
    # Add parameters here
    params = {"name": company_name}

    headers = {
        "X-RapidAPI-Key": "YOUR_API_KEY",
        "X-RapidAPI-Host": "company-clearbit.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    company_info = {
        "name": data.get("name"),
        "industry": data.get("category", {}).get("sector"),
        "location": data.get("location"),
        "employees": data.get("metrics", {}).get("employees")
    }
    return company_info
company_data = {
    "Infosys": {
        "name": "Infosys",
        "industry": "IT Services",
        "location": "Bangalore, India",
        "employees": 300000
    },
    "TCS": {
        "name": "Tata Consultancy Services",
        "industry": "IT Services",
        "location": "Mumbai, India",
        "employees": 600000
    },
    "Wipro": {
        "name": "Wipro",
        "industry": "IT Services",
        "location": "Bangalore, India",
        "employees": 250000
    },
    "HCL": {
        "name": "HCL Technologies",
        "industry": "IT Services",
        "location": "Noida, India",
        "employees": 220000
    },
    "Tech Mahindra": {
        "name": "Tech Mahindra",
        "industry": "IT Services",
        "location": "Pune, India",
        "employees": 150000
    },
    "Cognizant": {
        "name": "Cognizant Technology Solutions",
        "industry": "IT Services",
        "location": "Teaneck, New Jersey, USA",
        "employees": 350000
    }
}

def get_company_info(company_name: str):
    return company_data.get(company_name, {
        "name": None,
        "industry": None,
        "location": None,
        "employees": None
    })