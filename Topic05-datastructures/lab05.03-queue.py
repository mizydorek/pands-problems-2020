# Maciej Izydorek
# Queue program

import random

q = []
# Create q list filled in 10 random numbers from 0 to 100
for i in range(11):
    number = random.randint(1,101)
    q.append(number)
# print out q list
print('queue is', q)
# take and print out numbers from queue one at the time and
# current numbers still in the queue
# add one to lenght of q to check if list is empty and print out info
for i in range(len(q)+1): 
    if len(q) == 0:
        print('the queue is now empty')
        break
    #Inserted pop() into print to meets task criteria 
    print('current Number is', q.pop(0), q) 
# also added while loop which works and gives same output 
#while len(q) != 0:
#    print('current Number is', q.pop(0), q)    
#else:
#    print('the queue is now empty')   