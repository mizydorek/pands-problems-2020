# Maciej Izydorek
# Computing the primes

P = []
# loops through numbers from 0 to 100 and checking if it is prime
for i in range(2, 100):
    isprime = True
    # loops through values of P 
    for j in P:
        # see if j divides i
        if i % j == 0:
            # If it does, i is not a prime so exit loop and indicate it's not prime
            isprime = False
            break
    # If i is prime, then append to P 
    if isprime:
        P.append(i)
#print out list of primes
print(P)