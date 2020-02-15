# Maciej Izydorek
# prints out a random fruit
import random
# lists of fruits 
fruits = ('apple', 'banana', 'kiwi', 'orange', 'grapefruit', 'raspberry')
# random number starting at 0 up to length of list - 1 to do not get out of the list index
random = fruits[random.randint(0,len(fruits)-1)]

print('A random fruit: {}'.format(random))