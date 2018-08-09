import numpy as np
from math import fabs
# from integrate import trap_integrate


def trap_integrate(f, a, b, num_of_int=100):
    """
    integrate f over interval (a, b) there should be no singularities in the interval
    :param f: the function to be integrated
    :param a: interval lower bound
    :param b: interval upper bound
    :return: the numerical result of integral
    """

    # check the validity of input data
    if not a < b:
        raise ValueError('the lower bound a must be lesser the upper bound b')

    # evaluate the function overt the interval
    x = np.linspace(a, b, num=num_of_int)
    y = f(x)

    # the width of interval
    h = (b - a) / (num_of_int - 1)

    result = 2 * y.sum()
    result = result - y[0] - y[-1]
    result = result * h / 2

    return result


def simpson_integrate(f, a, b, num_of_int=100):
    """
    integrate f over interval (a, b) there should be no singularities in the interval
    :param f: the function to be integrated
    :param a: interval lower bound
    :param b: interval upper bound
    :return: the numerical result of integral
    """

    # check the validity of input data
    if not a < b:
        raise ValueError('the lower bound a must be lesser the upper bound b')

    # make the number of datums even
    if not num_of_int % 2 != 0:
        num_of_int += 1

    # evaluate the function overt the interval
    x = np.linspace(a, b, num=num_of_int)
    y = f(x)

    # remember the shape of array
    n = y.shape[0]
    # calculate the sum of even internal function values
    even_sum = y[2: n - 1: 2].sum() * 2
    # calculate the sum of odd function values
    odd_sum = y[1: n: 2].sum() * 4

    result = even_sum + odd_sum + y[0] + y[-1]

    result = result / 3 * (b - a) / (num_of_int - 1)

    return result


def romberg_integrate(f, a, b, order=6, verbose=False):
    # check the validity of input data
    if not a < b:
        raise ValueError('the lower bound a must be lesser the upper bound b')

    # init the romberg table
    rom_tab = np.zeros((order, order))
    # print(rom_tab)

    # number of intervals in first column
    ns = [2 ** val + 1 for val in range(order)]
    # print(ns)

    # first column values
    first_col = [trap_integrate(f, a, b, n) for n in ns]
    # print(first_col)

    # init first column
    first_col = np.array(first_col)
    rom_tab[:, 0] = first_col
    # print(rom_tab)

    # construct the table
    for j in range(1, order):
        for i in range(j, order):
            rom_tab[i, j] = (4 ** j * rom_tab[i, j - 1] - rom_tab[i - 1, j - 1]) / (4 ** j - 1)
    if verbose:
        print(rom_tab)

    result = rom_tab[order-1, order-1]
    del rom_tab
    return result
"""
def adaptive_int(f, a, b, int_method, eps=1e-10, init_num_int=100):
    \"""
    integrate f over (a, b) adaptively using a specific method
    :param f: the function to be integrated
    :param a: lower bound
    :param b: upper bound
    :param int_method: the base integrate method
    :param eps: the tolerance
    :return: the numerical integration result and step
    \"""

    # the stack of integration result
    stack_of_int = []

    # the number of interval
    num_of_interval = init_num_int

    # initialize the stack
    stack_of_int.append(int_method(f, a, b, num_of_interval))
    num_of_interval += 1
    stack_of_int.append(int_method(f, a, b, num_of_interval))

    while fabs(stack_of_int[1] - stack_of_int[0]) > eps:
        num_of_interval *= 2
        stack_of_int.pop(0)
        stack_of_int.append(int_method(f, a, b, num_of_interval))

    return stack_of_int[1], num_of_interval
"""



if __name__ == '__main__':
    def f(x):
        return x ** 2

    def g(x):
        return np.sin(x)

    def h(x):
        return np.sin(np.sqrt(100 * x)) ** 2


    print('trapezoidal:')
    integrate = trap_integrate(g, 0, 1)
    print(integrate)

    print('\nsimpson:')
    integrate = simpson_integrate(g, 0, 1)
    print(integrate)

    print('\nromberg:')
    integrate = romberg_integrate(g, 0, 1, verbose=True)
    print(integrate)
