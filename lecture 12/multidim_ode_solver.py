import numpy as np


def euler_solver(f, x, y_init):
    h = x[1] - x[0]
    if h < 0:
        raise ValueError('step size must be positive')
    
    y_init = np.array(y_init)
    shape = (x.shape[0], y_init.shape[0])
    y = np.zeros(shape)
    y[0] = y_init

    for i in range(1, shape[0]):
        y[i] = y[i - 1] + h * f(x[i-1], y[i-1])

    return y
