import requests
def GetData(url):
    response = requests.get(f"datos/{url}.json")
    return response.json()
