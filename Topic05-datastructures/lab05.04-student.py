# Maciej Izydorek
# Student program that stores a student name and 
# a list of courses and grades

student = {}

name = input('enter your name: ')
student['name'] = name
course = input('enter course: ')
grade = input('enter grade: ')

while True:
    student[course] = grade
    if course == '':
        break
    course = input('enter course: ')
    if grade == '':
        break
    grade = input('enter grade: ')

print(student)
#print('Student: {}'.format(student['name']))
