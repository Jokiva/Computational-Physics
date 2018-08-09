#!/home/jzhong/.anaconda3/bin/python
import numpy as np
import matplotlib.pyplot as plt

titles = ['Direct evaluation', 'Expanded evaluation', 'Horner\'s method'] 

print('single precision')
# read x data
f1 = open('x1.dat', 'r')
x = f1.read()
f1.close()
x = x.split('\n')
x.pop()
x = np.array(x, dtype=float)

names = ['y10.dat', 'y11.dat', 'y12.dat']
for j in range(3):
    # read y data
    f2 = open(names[j], 'r')
    y = f2.read()
    f2.close()
    y = y.split('\n')
    y.pop()
    y = np.array(y, dtype=float)

    # visualize
    plt.figure()
    plt.scatter(x, y, marker='x')
    plt.xlim(1-0.25, 1+0.25)
    plt.ylim(-5e-7, +5e-7)
    plt.title(titles[j]+' in single precision')
    plt.grid()
# plt.show()

print('double precision')
# read x data
f1 = open('x2.dat', 'r')
x = f1.read()
f1.close()
x = x.split('\n')
x.pop()
x = np.array(x, dtype=float)

names = ['y20.dat', 'y21.dat', 'y22.dat']
for j in range(3):
    # read y data
    f2 = open(names[j], 'r')
    y = f2.read()
    f2.close()
    y = y.split('\n')
    y.pop()
    y = np.array(y, dtype=float)

    # visualize
    plt.figure()
    plt.scatter(x, y, marker='x')
    plt.xlim(1-0.03, 1+0.03)
    plt.ylim(-5e-14, +5e-14)
    plt.title(titles[j]+' in double precision')
    plt.grid()
plt.show()