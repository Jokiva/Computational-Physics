import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from os import system
from time import time


t0 = time()
# deltas = (0, 0.5, 0.9)
deltas = [0.1 * i for i in range(9)]

try:
    rms = np.loadtxt('rms_1b.txt')
    print('data already exists')
except FileNotFoundError as exp:
    print(exp)
    print('this is an initial run. generating raw data') 
    system('python 1b_init.py')
    print('data generated')
    rms = np.loadtxt('rms_1b.txt')


# the data for fitting
# x_data = list(range(1000))
x_data = list(range(1, 1001))
# y_data = rms[-1]

# the fitting function
def fitting_fuc(x, a):
    return a * x ** 0.5


for n in range(10):
    y_data = rms[n]
    popt, pcov = curve_fit(fitting_fuc, x_data, y_data)
    print(popt)

print(time() - t0, 's elapsed')

