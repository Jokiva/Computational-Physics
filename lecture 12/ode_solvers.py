import numpy as np
import matplotlib.pyplot as plt


def euler_solver(f, x, y_init=0):
    """
    euler solver for increment function f
    f(x, y) = dy / dx
    :param f: the increment function
    :param x: evenly spaced ndarray of the interval on which y is obtianed
    :param y_init: the initial value of y
    :return: ndarray of y on the interval x
    """

    # the step size
    h = x[1] - x[0]

    y = np.zeros(x.shape[0])
    y[0] = y_init
    for i in range(1, x.shape[0]):
        y[i] = y[i - 1] + h * f(x[i-1], y[i-1])

    return y


def improved_euler_solver(f, x, y_init=0):
    """
    improved euler solver for increment function f
    f(x, y) = dy / dy
    :param f: the increment function
    :param x: evenly spaced ndarray of the interval on which y is obtianed
    :param y_init: the initial value of y
    :return: ndarray of y on the interval x
    """
    # the step size
    h = x[1] - x[0]

    y = np.zeros(x.shape[0])
    y[0] = y_init
    for i in range(1, x.shape[0]):
        s1 = f(x[i - 1], y[i - 1])
        s2 = f(x[i - 1] + h, y[i - 1] + h * s1)
        y[i] = y[i - 1] + h / 2 * (s1 + s2)
        # y[i] = y[i - 1] + h * f(x[i - 1], y[i - 1] + h / 2 * f(x[i-1], y[i-1]))

    return y


if __name__ == '__main__':
    def f(x, y):
        return np.sin(x) * x

    x = np.linspace(-1, 1)

    y1 = euler_solver(f, x)
    y2 = improved_euler_solver(f, x)

    plt.plot(x, y1, label='euler')
    plt.plot(x, y2, label='improved euler')
    plt.show()
