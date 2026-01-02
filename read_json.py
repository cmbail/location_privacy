import json         # import the Python json module

with open('fake_fruit.json', 'r') as f:  # open the JSON file for reading
    data = json.load(f)                  # de-serialise the JSON into data

print(data)         # data is a python dict containing the JSON data