# Maciej Izydorek
# Computing the primes
from functions import isprime

P = []
# loops through numbers from 0 to 100 and checking if it is prime
for i in range(2, 100):
    # else i is prime, then append to P 
    if isprime(i):
        P.append(i)
#print out list of primes
print(P)