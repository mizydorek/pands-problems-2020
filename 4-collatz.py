# Maciej Izydorek
# Collatz conjecture 

# variable to hold user input as integer
n = int(input("Please enter a positive number: "))

print(int(n), end=" ")
while n == 1:                   # validate if number is equal to one 
    n = 3 * n + 1                         # apply formula
    print(int(n), end=" ")               # and print out n 
else:
    while n != 1:               # statement that validates number from 2 up
        if n % 2 == 0:                   # check if it is even number
            n = n / 2                    # apply formula
            print(int(n), end=" ")       # print out n
        else:                            # check if it is odd number
            n = 3 * n + 1                # apply formula
            print(int(n), end=" ")       # print out n
print('')