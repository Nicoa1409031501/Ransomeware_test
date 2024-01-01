import requests

# Gathering victim network information using LookUP API
def gather_network_info():
    url = "https://api.lookup.ipify.org"
    response = requests.get(url)
    return response.json()

network_info = gather_network_info()
print(network_info)