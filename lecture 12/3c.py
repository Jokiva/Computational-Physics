from multidim_ode_solver import euler_solver
import numpy as np
import matplotlib.pyplot as plt

parent_tau = 2
daughter_taus = [0.02, 2, 200]

def f(x, y):
    n_p = y[0]
    n_d1 = y[1]
    n_d2 = y[2]
    n_d3 = y[3]

    f1 = - n_p / parent_tau
    f2 = n_p / parent_tau - n_d1 / daughter_taus[0]
    f3 = n_p / parent_tau - n_d2 / daughter_taus[1]
    f4 = n_p / parent_tau - n_d3 / daughter_taus[2]

    return np.array([f1, f2, f3, f4], dtype=float)

t = np.arange(0, 15, 0.001)
y = euler_solver(f, t, (1, 0, 0, 0))

plt.figure()
plt.plot(t, y[:, 0], label=r'Parent $\tau = 2$')
plt.plot(t, y[:, 1], label=r'Daughter $\tau = 0.02$')
plt.plot(t, y[:, 2], label=r'Daughter $\tau = 2$')
plt.plot(t, y[:, 3], label=r'Daughter $\tau = 200$')

#plt.xscale('log')
#plt.yscale('log')

plt.legend()
plt.grid()
plt.show()
