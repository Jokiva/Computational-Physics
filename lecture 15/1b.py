import numpy as np
import matplotlib.pyplot as plt
from os import system
from time import time


t0 = time()
# deltas = (0, 0.5, 0.9)
num_of_deltas = 10
deltas = [0.1 * i for i in range(10)]


# check if data generated
try:
    rms = np.loadtxt('rms_1b.txt')
    print('data already exists')
except FileNotFoundError as exp:
    print(exp)
    print('this is an initial run. generating raw data') 
    system('python 1b_init.py')
    print('data generated')
    rms = np.loadtxt('rms_1b.txt')
print(time() - t0, 's elapsed')    

system('python 1b_fit.py')

x = np.linspace(0, 1000, num=5000)
y = np.sqrt(x)

plt.figure()
for n in range(num_of_deltas):
    l = r'$\delta=$' + str(deltas[n]) 
    plt.scatter(list(range(1000)), rms[n], marker='+', label=l)
plt.plot(x, y, color='r', label=r'$\sqrt{N}$')

plt.legend()
plt.grid()
plt.show()
