from fitting import *
import numpy as np
import matplotlib.pyplot as plt


# linear function
def f(x, coeffs):
    if len(coeffs) != 2:
        raise ValueError('the length of coefficient array should be two')
    return coeffs[0] + coeffs[1] * x


# data 1
x_1 = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
y_1 = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68])

# data 2
x_2 = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
y_2 = np.array([9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74])

# data 3
x_3 = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
y_3 = np.array([7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73])

# data 4
x_4 = np.array([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8])
y_4 = np.array([6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89])

xs = [x_1, x_2, x_3, x_4]
ys = [y_1, y_2, y_3, y_4]

for i in range(4):
    # get the fit result
    coeff = linear_fit(xs[i], ys[i])

    # create the range for evaluation
    x = np.linspace(xs[i].min(), xs[i].max())
    # the fitted data
    y = evaluate_linear_result(x, coeff)

    # make a plot
    plt.figure()
    plt.title('Data ' + str(i+1))
    plt.scatter(xs[i], ys[i], color='r')
    plt.plot(x, y)
    plt.grid()

plt.show()
