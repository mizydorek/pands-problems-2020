# Maciej Izydorek
# program counts how many times it was run 

filename = 'count.txt'

def readFile():
    with open(filename, 'r') as reader:
        number = int(reader.read())     # converts str to int
        return number

def writeFile(number):
    with open(filename, 'w') as writer:
        writer.write(str(number))       # write takes str 

# main
number = readFile()
number += 1
print('Program has been run {} times'.format(number))
writeFile(number)