import os
import json
import requests

url = "https://sonujson-devloper.vercel.app/Data/sports.json"
response = requests.get(url)
data = response.json()

os.makedirs("Data", exist_ok=True)

with open("Data/subho_sports.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("✅ subho_sports.json updated successfully!")
