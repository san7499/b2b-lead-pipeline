import json


def clean_data():
    try:
        with open("data/raw.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print("❌ Error loading raw data:", e)
        return []

    cleaned = []
    seen = set()

    for item in data:
        try:
            name = str(item.get("name", "")).strip()
            description = str(item.get("description", "")).strip()

            if not name:
                continue

            # remove duplicates
            if name in seen:
                continue
            seen.add(name)

            cleaned.append({
                "name": name,
                "description": description if description else "N/A"
            })

        except:
            continue

    try:
        with open("data/cleaned.json", "w", encoding="utf-8") as f:
            json.dump(cleaned, f, indent=4)
    except Exception as e:
        print("❌ Error saving cleaned data:", e)
        return []

    print(f"✅ Cleaned {len(cleaned)} records")

    return cleaned


if __name__ == "__main__":
    clean_data()