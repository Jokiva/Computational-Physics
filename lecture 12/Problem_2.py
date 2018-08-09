from difference import forward_diff, central_diff
import numpy as np
import matplotlib.pyplot as plt

# alias for the exponential function
def f(x):
    return np.exp(-x)
def g(x):
    return - np.exp(-x)

# containers for the errors
forward_error = []
central_error = []

# evluation parameters
x0 = 3
hs = np.logspace(-12, 2, 10000)
# hs = np.linspace(0.1, 20, 100)
analytical = g(x0)

# calculate the errors
for h in hs:
    forward = forward_diff(f, x0, h)
    central = central_diff(f, x0, h)

    forward_error.append(abs((forward - analytical) / analytical))
    central_error.append(abs((central - analytical) / analytical))


# plot the result
plt.figure()
plt.plot(hs, forward_error, label='Forward')
plt.plot(hs, central_error, label='Central')

plt.title('Differentiating Error of $f(x) = e^{-x}$')
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.grid()
plt.show()