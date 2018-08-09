import numpy as np
import matplotlib.pyplot as plt
from integrate import *
from math import sqrt, pi, fabs
from fitting import *


def f(x):
    return 1 / (1 + x ** 2)


targets = [10**(-val) for val in range(2, 13)]

trap_nums = [1 / sqrt(target) for target in targets]
trap_nums = [int(val) for val in trap_nums]
# simp_err = [fabs(simpson_integrate(f, 0, 1, num) - pi / 4) for num in simp_nums]
trap_err = []
for n in trap_nums:
    res = trap_integrate(f, 0, 1, n)
    trap_err.append(fabs(res - pi / 4))


# evaluate the log of data
log_nums = np.log10(trap_nums)
log_err = np.log10(trap_err)

plt.figure()
plt.scatter(log_nums, log_err, color='r')
# plt.xscale('log')
# plt.yscale('log')
plt.title('Trapezoidal method')
plt.xlabel('number of sub-intervals')
plt.ylabel('error')
plt.grid()
# plt.show()

fit_res = linear_fit(log_nums, log_err)
print(fit_res)
x = np.linspace(log_nums.min(), log_nums.max())
y = np.array(evaluate_linear_result(x, fit_res))

plt.plot(x, y)
if fit_res[1] > 0:
    func_name = '$%.2f + %.2f x$' % tuple(fit_res)
else:
    func_name = '$%.2f - %.2f x$' % tuple([fit_res[0], fabs(fit_res[1])])

plt.annotate(func_name,
            xy=(5, -11.5), xycoords='data',
            xytext=(-70, 0), textcoords='offset points',
            arrowprops=dict(facecolor='green', shrink=0.05),
            horizontalalignment='right',
            verticalalignment='bottom')


plt.show()