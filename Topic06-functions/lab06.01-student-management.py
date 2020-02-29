# Maciej Izydorek
# Student management program
students = []
# function that display menu
def displayMenu():
    print('What would you like to do?')
    print('\t(a) Add new student')
    print('\t(v) View students')
    print('\t(q) Quit')
    choice = input('Type one letter (a/v/q):')
    return choice
# add function which creates current student dict, takes student
# name as an input and refers module field to add module function 
def doAdd():
    currentStudent = {}
    currentStudent['name'] = input('enter name: ')
    currentStudent['modules'] = addModules()
    students.append(currentStudent)
# modules function that takes modules and grades as an input and 
# quit the loop if module name equals blank 
def addModules():
    modules = []
    moduleName = input('enter the first Module name(blank to quit): ')
    while moduleName != '':
        module = {}
        module['name'] = moduleName
        module['grade'] = int(input('enter grade: '))
        modules.append(module)
        moduleName = input('enter next module name(blank to quit): ')
    return modules
# displays modules of student by looping through the modules dict
def displayModules(modules):
    for module in modules:
        print('{} : {}'.format(module['name'],module['grade'])) 
# display function that loops through students dict to output name
# refers to display modules function to output all modules
def doView():
    for student in students:
        print(student['name'])
        displayModules(student['modules'])
# displays main menu and waits for user to choose an option
choice = displayMenu()
while choice != 'q':
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice != 'q':
        print('\nplease select either a,v or q')
    choice = displayMenu()