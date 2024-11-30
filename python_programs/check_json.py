import json

# Load the JSON file
try:
    with open("articles1.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    print("JSON is valid!")
except json.JSONDecodeError as e:
    print("JSON is invalid:", e)
    exit()

# Check each article for issues
for index, article in enumerate(data):
    print(f"\nChecking article {index + 1}: {article.get('title', 'No title provided')}")

    # Check for missing fields
    required_fields = ["title", "url", "description", "tags"]
    for field in required_fields:
        if field not in article:
            print(f"  - Missing field: {field}")

    # Check for empty description
    if not article.get("description"):
        print("  - Description is empty")

    # Check for duplicate tags
    tags = article.get("tags", [])
    if len(tags) != len(set(tags)):
        print("  - Duplicate tags found:", [tag for tag in tags if tags.count(tag) > 1])

    # Check URL validity (basic validation)
    url = article.get("url", "")
    if not url.startswith("http://") and not url.startswith("https://"):
        print("  - URL might be invalid:", url)

# Optional: Remove duplicates in tags and save back to the file
for article in data:
    if "tags" in article:
        article["tags"] = list(set(article["tags"]))  # Deduplicate tags

# Save the cleaned JSON file
with open("articles_cleaned.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("\nValidation and cleaning completed. Cleaned data saved to 'articles_cleaned.json'.")

