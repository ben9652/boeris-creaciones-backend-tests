import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def fetch_data(url):
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

response = fetch_data('https://localhost:7153/api/Unidades')

print(response)
