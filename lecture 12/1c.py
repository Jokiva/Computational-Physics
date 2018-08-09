import numpy as np
import matplotlib.pyplot as plt
from ode_solvers import *
from fitting import *


def f(x, y):
    return 1 - x + 4 * y


def g(x):
    return 1 / 16 * (-3 + 19 * np.exp(4 * x) + 4 * x)


standard = g(1)

# generate different steps
# hs = [1/ 10 ** i for i in range(1, 7)]
hs = np.logspace(-7, -1)
# containers for errors
euler_errors = []
improved_euler_errors = []
# try different steps
for h in hs:
    x = np.arange(0, 1, h)
    
    # solve with different methods
    y_euler = euler_solver(f, x, 1)
    euler_errors.append(np.abs(y_euler[-1] - standard))

    y_improved_euler = improved_euler_solver(f, x, 1)
    improved_euler_errors.append(np.abs(y_improved_euler[-1] - standard))
    del x


# print the errors
print(euler_errors)
print(improved_euler_errors)

# we may convert the data into log scale
hs = np.log10(hs)
euler_errors = np.log10(euler_errors)
improved_euler_errors = np.log10(improved_euler_errors)

# fit the data
x = np.linspace(hs[0], hs[-1])
para = linear_fit(hs, euler_errors)
print(para)
y1 = evaluate_linear_result(x, para)

para = linear_fit(hs, improved_euler_errors)
print(para)
y2 = evaluate_linear_result(x, para)

plt.figure()
# we may convert the errors
plt.scatter(hs, euler_errors, label='Euler')
plt.plot(x, y1)
plt.scatter(hs, improved_euler_errors, label='Improved Euler')
plt.plot(x, y2)
plt.legend()
plt.grid()
plt.show()
