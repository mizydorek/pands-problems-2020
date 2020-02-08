# Maciej Izydorek
# Collatz conjecture

n = int(input("Please enter a positive number: "))

print(int(n))
while n == 1:
    n = 3 * n + 1
    print(int(n))
else:
    while n != 1:
        if n % 2 == 0: 
            n = n / 2
            print(int(n))
        else:
            n = 3 * n + 1
            print(int(n))