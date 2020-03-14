# Maciej Izydorek
# program counts how many times it was run 
import os.path

filename = 'count.txt'

if not os.path.isfile(filename):
    print('File does not exsist')
    # init file here
    writeNumber(0)

def readNumber():
    try:
        with open(filename, 'r') as reader:
            number = int(reader.read())     # converts str to int
            return number
    except IOError:
        # no file - first run
        return 0

def writeNumber(number):
    with open(filename, 'w') as writer:
        writer.write(str(number))       # write takes str 

# main
number = readNumber()
number += 1
print('Program has been run {} times'.format(number))
writeNumber(number)