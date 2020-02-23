# Maciej Izydorek
# Program which takes a positive float number as input and 
# outputs an approximation of its square root
import math

# square root function which takes inputed float number 
# outputs square root of it rounded to one decimal place
def sqrt(f):
    num = round(math.sqrt(f),1)
    return num 
# stores inputed positive float number  
f = float(input('Enter a positive number: '))
# Prints out the result in desired format 
print('The square root of {} is approx. {}'.format(f,sqrt(f)))