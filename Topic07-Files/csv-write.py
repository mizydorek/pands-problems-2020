import csv
# writing to csv
'''
with open('employee.csv', 'w') as writer:
    employee = csv.writer(writer, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee.writerow(['John Smith', 'Accounting', 'November'])
    employee.writerow(['Erica Mayers', 'IT', 'March'])
'''
# writing to csv from dictionary
with open('employee.csv' , 'w') as emplyeee_file:
    fieldnames = ['name', 'dept', 'month']
    writer = csv.DictWriter(emplyeee_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'name':'John Smith', 'dept':'Accounting', 'month':'November'})
    writer.writerow({'name':'Erica Meyers', 'dept':'IT', 'month':'March'})