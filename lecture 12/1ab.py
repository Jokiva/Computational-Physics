from ode_solvers import *
from fitting import *
import matplotlib.pyplot as plt

# the differetnial equation to be solved
def f(x, y):
    return 1 - x + 4 * y

# anatical result
def g(x):
    return 1 / 16 * (-3 + 19 * np.exp(4 * x) + 4 * x)

# the 
x = np.linspace(0, 1, 100000)

y = g(x)
y1 = euler_solver(f, x, 1)
y2 = euler_solver(f, x, 1)


# comapare the three methods
plt.figure()
plt.plot(x, y, label='analytical')
plt.plot(x, y1, label='euler')
plt.plot(x, y2, label='improved euler')
plt.grid()
plt.legend()
plt.show()
