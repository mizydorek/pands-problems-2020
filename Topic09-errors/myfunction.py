# Calculate factorial of a number

def factorial(n):
    ''' Returns the factorial of n.
    e.g. factorial(7) = 7x76x5x4x3x2x1 = 5040.
    '''

    answer = 1
    for i in range(1,n+1):
        answer = answer * i

    return answer

if __name__ == "__main__":
    assert factorial(7) == 5040