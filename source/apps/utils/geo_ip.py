import requests

def get_location():
    response = requests.get('http://ip-api.com/json')
    return response.json()
