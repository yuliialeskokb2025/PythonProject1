import requests

def fetch_ip():
    """" Sends HTTP GET-request to AIP ipify and returns public IP-address """
    response = requests.get('https://api.ipify.org?format=json')
    return response.json()['ip']