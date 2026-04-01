import json

def clean_data():
    with open("data/raw.json") as f:
        data = json.load(f)

    cleaned = []

    for company in data:
        cleaned.append({
            "name": company.get("name", "N/A"),
            "description": company.get("description", "N/A").lower()
        })

    with open("data/cleaned.json", "w") as f:
        json.dump(cleaned, f, indent=4)

    return cleaned