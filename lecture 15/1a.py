import numpy as np
import matplotlib.pyplot as plt
from os import system
from time import time


t0 = time()

try:
    rms = np.loadtxt('rms_1a.txt')
    print('data already exists')
except FileNotFoundError as exp:
    print(exp)
    print('this is an initial run. generating raw data') 
    system('python 1a_init.py')
    print('data generated')
    rms = np.loadtxt('rms_1b.txt')


print(time() - t0, 's elapsed')    

num_of_paths = (50, 500, 5000)
x = np.linspace(0, 1000, 2000)
y = np.sqrt(x)


plt.figure()
for n in range(3):
    l = str(num_of_paths[n]) + ' paths' 
    plt.scatter(list(range(1000)), rms[n], marker='+', label=l)
plt.plot(x, y, color='c', label=r'$\sqrt{N}$')

plt.legend()
plt.grid()
plt.show()