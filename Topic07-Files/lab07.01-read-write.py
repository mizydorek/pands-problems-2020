# Maciej Izydorek
# program counts how many times it was run 

filename = 'count.txt'

def readNumber():
    with open(filename, 'r') as reader:
        number = int(reader.read())
        return number
        
def writeNumber(number):
    with open(filename, 'w') as writer:
        writer.write(str(number)) 

writeNumber(0)
print(readNumber())