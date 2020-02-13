# Maciej Izydorek 
# Program generate and prints 10 random numbers from 0 to 100 
# prints them out and then prints out top three
import random

numbers = []

for i in range(11):
    # random function generates random number from 0 - 100 
    number = random.randint(1,101)
    numbers.append(number)

print(numbers)
# sort numbers in reverse order and print top three
numbers.sort(reverse=True)
print(numbers[:3])