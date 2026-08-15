import os
import json
import requests

url = "https://sonujson-v3.pages.dev/Data/sports.json"
response = requests.get(url)
data = response.json()

os.makedirs("Data", exist_ok=True)

with open("Data/subhotv.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
