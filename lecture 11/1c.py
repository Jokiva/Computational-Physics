from integrate import*
import numpy as np


def f_1(x):
    return 2 / (1 + x ** 2)


def f_2(x):
    return 2 / (1 + x ** 2)


I_1 = romberg_integrate(f_1, 0, 1)
I_2 = romberg_integrate(f_2, 0, 1)
I = I_1 + I_2

print(I)
