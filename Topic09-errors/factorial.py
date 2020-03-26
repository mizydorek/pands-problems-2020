import sys
import myfunction

# Get n from the command line.
n = int(sys.argv[1])
# Calculate the factorial of n
ans = myfunction.factorial(n)
# print answer
print("The factorial of", n, "is:", ans)