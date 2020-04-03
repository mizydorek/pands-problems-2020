# Maciej Izydorek
# week 8 task - comparison of three function 
# f(x) = x, g(x) = x**2, h(x) = x**3

import matplotlib.pyplot as plt
import numpy as np

# generate 100 linearly spaced numbers in range 0-4
x = np.linspace(0.0, 4.0, 100)

# the functions 
f = x
g = x**2
h = x**3 

# plot the functions and add labels
plt.plot(x, f, 'b', label = 'f(x) = x')
plt.plot(x, g, 'g', label = 'g(x) = x**2')
plt.plot(x, h, 'r', label = 'h(x) = x**3')

# setting the plot 
plt.title("Comparison of functions")
plt.legend()
plt.xlabel("x(in range 0-4)")

# create png and show the plot 
plt.savefig("comparison.png")
plt.show()