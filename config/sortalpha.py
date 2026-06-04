import json

contents = {}
with open("./artifacts.json", "r") as file:
    contents = json.load(file)


contents = sorted(contents, key=lambda item: item['name'].lower())

with open("artifacts.json", "w") as file:
    json.dump(contents, file)