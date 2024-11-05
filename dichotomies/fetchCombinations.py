import json
import requests
import os

jsonUrl = "https://raw.githubusercontent.com/andylehti/Triadic-Personality-Framework/main/dichotomies/coding.json"
jsonPath = "coding.json"

if not os.path.exists(jsonPath):
    res = requests.get(jsonUrl)
    if res.status_code == 200:
        with open(jsonPath, "w") as f:
            f.write(res.text)
        print("Downloaded JSON file.")
    else:
        print("Failed to download JSON file.")
        exit(1)

with open(jsonPath, "r") as f:
    data = json.load(f)

def showMatch(personality):
    for cat, items in data.items():
        print(f"\n### {cat.capitalize()}\n")
        print("| Code | Name | Category | " + " | ".join([f"{cat} {i+1}" for i in range(10)]) + " |")
        print("|------|------|----------| " + " | ".join(["---"] * 10) + " |")
        
        for code, entries in items.items():
            if all(c in personality for c in code):
                name = f"{cat.capitalize()} {code}"
                row = f"| {code} | {name} | {cat.capitalize()} | " + " | ".join(entries[:10]) + " |"
                print(row)

personalityInput = "INFP"
showMatch(personalityInput)
