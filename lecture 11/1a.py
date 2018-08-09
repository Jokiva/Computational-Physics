from integrate import *
import numpy as np


# anatical result
ana_res = np.pi / 2

# integrands
def f(x):
    return np.sqrt(1 - x ** 2)


def g(x):
    return np.sin(x) ** 2


# using different forms to integrate
res_1 = simpson_integrate(f, -1, 1)
res_2 = simpson_integrate(g, 0, np.pi)

print(res_1, res_1 - ana_res)
print(res_2, res_2 - ana_res)