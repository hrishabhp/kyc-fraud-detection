import requests
from tests.config.settings import BASE_URL

def get(endpoint: str):
    """Reusable GET request wrapper"""
    url = f"{BASE_URL}{endpoint}"
    return requests.get(url)

def post(endpoint: str, data: dict):
    """Reusable POST request wrapper"""
    url = f"{BASE_URL}{endpoint}"
    return requests.post(url, json=data)



