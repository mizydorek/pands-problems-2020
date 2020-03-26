# Maciej Izydorek
# Topic09 errors and exceptions 

import sys

try:
    with open(sys.argv[1]) as f:
        print(f.read())
    a = 1 / 0
except FileNotFoundError:
    print("File " + sys.argv[1] + ' does not exsist.')
except:
    print('This is zero division error handler.')