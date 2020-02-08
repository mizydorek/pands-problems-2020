# Maciej Izydorek
# Collatz conjecture 

n = int(input("Please enter a positive number: "))

print(int(n))
while n == 1:                   # validates if number is equal to one 
    n = 3 * n + 1               
    print(int(n))
else:
    while n != 1:               # statement that validates number from 2 up
        if n % 2 == 0:          # checks if it is even number
            n = n / 2
            print(int(n))
        else:                   # checks if it is odd number
            n = 3 * n + 1
            print(int(n))