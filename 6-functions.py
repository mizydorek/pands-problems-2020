# Function to square numbers
import math 

def power(x, y):
    ans = x
    y = y - 1
    while y > 0:
        ans = ans * x
        y = y - 1
    return ans 

def f(x):
    ans = ((100 * power(x, 2)) + 10 * power(x, 3)) // 100
    ans = ans - (power(x, 3)) // 10
    return ans 

def isprime(i):
    # loops through values from 2 up to but not including i
    for j in range(2, math.floor(math.sqrt(i)))ł:
    # See if j divides i.
        if i % j == 0:
            # If it does, i is not a prime so return False
            return False
    return True