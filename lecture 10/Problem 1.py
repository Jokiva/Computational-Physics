import numpy as np
import matplotlib.pyplot as plt
from integrate import *


def calc_capacity(T, num=50):
    # constants in the problem
    # volume of solid
    V = 1000 / 1e6
    # density o atoms
    rho = 6.022e28
    # boltzmann's constant
    k_b = 1.3906e-23
    # debye temperature
    theta_d = 428

    def integrand(x):
        return x ** 4 * np.exp(x) / ((np.exp(x) - 1) ** 2)

    result = simpson_integrate(integrand, 0+1e-9, theta_d / T, num_of_int=num)
    result = 9 * V * rho * k_b * (T / theta_d) ** 3 * result

    return result


try:
    t = np.linspace(0, 500, 10000)
    cap = [calc_capacity(val) for val in t]
except RuntimeError:
    pass

plt.figure()
plt.title('Debye model')
plt.plot(t, cap, label='Aluminium')
plt.legend()
plt.xlabel(r'$T / $' + 'K')
plt.ylabel(r'$C_v / $' + '$($' + 'J/K' + '$^{-1})$')
plt.grid()
plt.show()

exit()

