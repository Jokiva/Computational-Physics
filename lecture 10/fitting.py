import numpy as np


def linear_fit(x_data, y_data):
    # check the validity of input
    if x_data.shape != y_data.shape:
        raise ValueError('the input data must be the same length')

    # calculate the product of x_data and y_data
    product = x_data * y_data
    # calculate the square of x and y
    x_square = x_data ** 2
    # y_square = y_data ** 2

    a_0 = (y_data.mean() * x_square.mean() - x_data.mean() * product.mean()) / (x_square.mean() - x_data.mean() ** 2)
    a_1 = (product.mean() - x_data.mean() * y_data.mean()) / (x_square.mean() - x_data.mean() ** 2)

    return np.array([a_0, a_1])


def evaluate_linear_result(x, coeff):
    if len(coeff) != 2:
        raise ValueError('the number if parameters must be two')
    l = [coeff[0] + val * coeff[1] for val in x]
    return l

