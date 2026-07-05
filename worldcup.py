import requests

from config import DATA_URL

response = requests.get(DATA_URL, timeout=10)

response.raise_for_status()

data = response.json()

matches = data["matches"]

print(len(matches))