# Maciej Izydorek
# csv
import csv
"""
with open('employee.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0 
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
"""

'''
with open('employee.txt') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0 
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')

with open('employee.txt', 'r') as reader:
    employee = csv.reader(reader, delimiter=',')
    for row in employee:
        print(', '.join(row))
'''
with open('employee.txt', 'r') as reader:
    employee = csv.DictReader(reader)
    for row in employee:
        print(f"{row['name']}")