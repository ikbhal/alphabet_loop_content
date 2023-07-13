import json

# Read the JSON file
with open('states_languages.json') as file:
    data = json.load(file)

# Extract the languages
languages = set(entry['primary_language'] for entry in data['states'])

# Print the unique languages
print("Unique Languages:")
for language in languages:
    print(language)
