# Maciej Izydorek
# Reads in two numbers, divides them and outputs integer result and
# the remainder 

x = int(input('enter first number: '))
y = int(input('enter second number: '))
# makes output more dynamic with if statement 
if x % y == 0:
    # convert result of division to int
    z = int(x / y)
    print("{} divided by {} is {} ".format(x, y, z))
else:
    # convert result of division to int
    z = int(x / y)
    remainder = x % y
    print("{} divided by {} is {} with remainder {}".format(x, y, z, remainder))