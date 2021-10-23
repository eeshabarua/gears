import requests

URL = "https://www.causeiq.com/organizations/"
page = requests.get(URL)

print(page.content)