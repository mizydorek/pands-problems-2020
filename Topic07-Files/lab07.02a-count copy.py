# Maciej Izydorek
# program counts how many times it was run 

filename = 'count.txt'

def readNumber():
    with open(filename, 'r') as reader:
        number = int(reader.read())     # converts str to int
        return number

def writeNumber(number):
    with open(filename, 'w') as writer:
        writer.write(str(number))       # write takes str 

# main
number = readNumber()
number += 1
print('Program has been run {} times'.format(number))
writeNumber(number)