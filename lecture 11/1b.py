from integrate import *
import numpy as np
import matplotlib.pyplot as plt


# this function generates a series of functions
# with different ks
def gen_f(a, b, nums=100):
    def f(k):
        # no looping variables in the return function
        def g(x):
            # k is referred as parameter of f
            return 1 / np.sqrt(1 - k ** 2 * np.sin(x) ** 2)
        return g

    fs = []
    ks = np.linspace(a, b, nums)
    for k in ks:
        fs.append(f(k))

    return fs


n = 10000
# generate a series of functions
fs = gen_f(0, 1, n)
# the range of k
k = np.linspace(0, 1, n)
y = [simpson_integrate(func, 0, np.pi / 2) for func in fs]


plt.figure()
plt.plot(k, y)

plt.grid()
plt.title('Complete Elliptic Integral of the First Kind')
plt.xlabel('$k$')
plt.ylabel('$y$')
plt.yticks([np.pi / 2, np.pi, 3 / 2 * np.pi], [r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3}{2} \pi$'])
plt.annotate('$E(k)$',
            xy=(1, 3 / 2 * np.pi), xycoords='data',
            xytext=(-70, 0), textcoords='offset points',
            arrowprops=dict(facecolor='green', shrink=0.05),
            horizontalalignment='right',
            verticalalignment='bottom')
plt.show()
