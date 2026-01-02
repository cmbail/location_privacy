import json

def addStrawberry():
    with open('fake_fruit.json', 'r') as f:   
        data = json.load(f)                   
        data['Fruit'].append({
            'Name': 'Strawberry',
            'Colour': 'Red'
            })
    return data

print(addStrawberry())