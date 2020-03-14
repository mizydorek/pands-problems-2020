# Maciej Izydorek
# Student management program
import json 

students = []
filename = 'students.json'

def writeDict(obj):
    with open(filename, 'wt') as f:
        json.dump(obj,f)

def readDict():
    with open(filename) as f:
        return json.load(f)

# function that display menu
def displayMenu():
    print('What would you like to do?')
    print('\t(a) Add new student')
    print('\t(v) View students')
    print('\t(s) Save students')
    print('\t(q) Quit')
    choice = input('Type one letter (a/v/q):')
    return choice

# add function
def doAdd():
    print('in adding')
# view function
def doView():
    print('in viewing')
# save function
def doSave():
    writeDict(students)
    print('students saved')
# load function
def doLoad():
    global students
    students = readDict()
    print('students loaded')

# Main
# displays main menu and waits for user to choose an option
choice = displayMenu()
while choice != 'q':
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice == 'l':
        doLoad()
    elif choice == 's':
        doSave()
    elif choice != 'q':
        print('\nplease select either a,v,l,s or q')
    choice = displayMenu()