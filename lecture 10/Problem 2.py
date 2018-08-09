from integrate import *
# from math import sqrt, sin
import numpy as np


# integrand
def f(x):
    return np.sin(np.sqrt(100 * x)) ** 2


ANA_RES = (201 - np.cos(20) - 20 * np.sin(20)) / 400


def find_num(f, int_met, a, b, init_num, ana_res, eps=1e-10):
    nums = init_num
    err = np.abs(ana_res - int_met(f, a, b, nums))

    while err > eps:
        nums += 2
        res = int_met(f, a, b, nums)
        err = np.abs(res - ana_res)

    return nums


n = find_num(f, simpson_integrate, 0, 1, 1000, ANA_RES)
print(n)

n = find_num(f, trap_integrate, 0, 1, 280000, ANA_RES)
print(n)

# print(trap_integrate(f, 0, 1, 280000) - ANA_RES)

exit()
