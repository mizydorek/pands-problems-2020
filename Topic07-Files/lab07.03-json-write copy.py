# Maciej Izydorek
# function to store data in json 
import json 

filename = 'testdata.json'

d = dict(name = 'Fred', age=31, grades=[1,34,55])

def writeFile(obj):
    with open(filename, 'w') as f:
        json.dump(obj, f)

writeFile(d)