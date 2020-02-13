# Maciej Izydorek 
# Program reads students until the user eneter blank 
# and prints all of them

students = []

firstname = input('enter firstname (blank to quit): ').strip()

while firstname != '':
    student = {}
    student['firstname'] = firstname
    lastname = input('enter lastname: ').strip()
    student['lastname'] = lastname
    students.append(student)
    # next student
    firstname = input('enter firstname (blank to quit): ').strip()

print('Here are the students you entered:')

for currentStudent in students:
    print("{} {}".format(currentStudent['firstname'], currentStudent['lastname']))