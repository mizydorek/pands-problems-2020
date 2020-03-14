# Maciej Izydorek
# function to store data in json 
import json 

filename = 'testdata.json'

def readFile():
    with open(filename, 'r') as f:
        return json.load(f)

print(readFile())