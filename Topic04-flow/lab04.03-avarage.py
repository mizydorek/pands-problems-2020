# Maciej Izydorek
# Program reads in numbers until user enters 0 
# then prints numbers and their avarage

numbers = []
# reads first number then we check if it is 0 in the while loop
number = int(input('enter number (0 to quit): '))

while number != 0:
    numbers.append(number)
    # read the next number and check if it is 0
    number = int(input('enter number (0 to quit): '))
# print numbers
for value in numbers:
    print(value)
# calculate their avarage
avarage = float(sum(numbers)) / len(numbers)
print('The avarage is {}'.format(avarage))