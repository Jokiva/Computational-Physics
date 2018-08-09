from ode_solvers import euler_solver
import numpy as np
import matplotlib.pyplot as plt

tau = 2
# the deriative
def f(x, y):
    return - y / tau


# the analytical result
def g(x):
    return np.exp(- x / tau)


# different steps
hs = [1, 0.1, 0.01]
# the time interval on which the equation will be solved
ts = [np.arange(0, 15, h) for h in hs]


# solve the equation on for different h
numerical_solutions = [euler_solver(f, t, 1) for t in ts]
# the analycital result
analytical_solutions = [g(t) for t in ts]
# compute the errors
errors = [np.abs((numerical_solution - analytical_solution) / analytical_solution) for numerical_solution, analytical_solution in zip(numerical_solutions, analytical_solutions)]


# plot the numerical result
plt.figure()
for i in range(3):
    plt.plot(ts[i], numerical_solutions[i], label='$h = {}$'.format(hs[i]))
plt.title(r'Solving $N ^ {\prime} (t) = - N(t) / \tau$')
plt.grid()
plt.legend()
# plt.show()


# plot the error
plt.figure()
for i in range(3):
    plt.plot(ts[i], errors[i], label='$h = {}$'.format(hs[i]))
plt.title('Errors for different step size')
plt.grid()
plt.legend()
plt.show()