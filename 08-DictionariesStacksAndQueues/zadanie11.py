import json

with open("data.json") as file:
    data = json.load(file)

for dict in data:
    for k,v in dict.items():
        print(k,":",v)

