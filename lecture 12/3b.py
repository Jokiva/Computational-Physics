from ode_solvers import euler_solver
import numpy as np
import matplotlib.pyplot as plt

taus = [5, 3, 1, 0.1, 0.01]

# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。 
# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变
def derivative_generator():
    derivatives = []
    for tau in taus:
        def f(tau):
            #def g(x, y):
            #    return - y / tau
            # 使用匿名函数可以缩减代码
            return lambda x, y: - y / tau

        derivatives.append(f(tau))
    return derivatives


def analytical_generator():
    analyticals = []
    for tau in taus:
        def f(tau):
            def g(x):
                return np.exp(- x / tau)
            return g
        analyticals.append(f(tau))

        return analyticals


h = 0.01
t = np.arange(0, 15, h)
derivatives = derivative_generator()
numerical_solutions = [euler_solver(f, t, 1) for f in derivatives]


plt.figure()
for i in range(5):
    plt.plot(t, numerical_solutions[i], 
             label=r'$\tau = {}$'.format(taus[i]))
plt.grid()
plt.legend()
#plt.xscale('log')
#plt.yscale('log')
plt.show()


# test codes for enclosure
#f0, f1, f2, f3, f4 = derivative_generator()
#x = np.linspace(0, 15)
#x0 = np.linspace(0, 15)
#y0 = f0(x0, x)
#y1 = f1(x0, x)
#y2 = f2(x0, x)

#plt.plot(x, y0, x, y1, x, y2)
#plt.show()
