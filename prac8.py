import json

with open('data.json', 'r') as file:
    data = json.load(file)
with open('data2.json', 'w') as f:
    json.dump(data,f,indent = 4)
with open('data2.json', 'r') as f:
    neyga = json.load(f)

print(neyga)