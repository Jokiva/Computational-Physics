import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, pi, fabs
from integrate import *
from fitting import *


def f(x):
    return 1 / (1 + x ** 2)


targets = [10**(-val) for val in range(2, 13)]


comp_bound = 7
rom_nums = [1 / target ** (1 / 6) for target in targets[0: comp_bound]]
rom_nums = [int(val) for val in rom_nums]
rom_err = []
for n in rom_nums:
    res = romberg_integrate(f, 0, 1, n)
    rom_err.append(fabs(res - pi / 4))
    # pass

# evaluate the log of data
log_nums = np.log10(rom_nums)
log_err = np.log10(rom_err)

plt.figure()
plt.scatter(log_nums, log_err, color='r')
# plt.xscale('log')
# plt.yscale('log')
plt.title('Romberg\'s method')
plt.xlabel('number of sub-intervals')
plt.ylabel('error')
plt.grid()
# plt.show()

fit_bound = 7
fit_res = linear_fit(log_nums[:fit_bound], log_err[:fit_bound])
x = np.linspace(log_nums.min(), log_nums.max())
y = np.array(evaluate_linear_result(x, fit_res))

plt.plot(x, y)
if fit_res[1] > 0:
    func_name = '$%.2f + %.2f x$' % tuple(fit_res)
else:
    func_name = '$%.2f - %.2f x$' % tuple([fit_res[0], fabs(fit_res[1])])

plt.annotate(func_name,
            xy=(1.1, -15), xycoords='data',
            xytext=(-70, 0), textcoords='offset points',
            arrowprops=dict(facecolor='green', shrink=0.05),
            horizontalalignment='right',
            verticalalignment='bottom')


plt.show()

