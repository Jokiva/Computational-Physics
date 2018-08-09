# import packages
import numpy as np
import matplotlib.pyplot as plt


# the integrand
def f(y):
    return 2 / (2 + y)


if __name__ == '__main__':
    # the interval on which the integral will be performed
    num_of_samp = 1000000
    x = np.random.uniform(0, 2, num_of_samp)
    # the sampling result
    y = f(x)

    # calculate the mean
    y_ave = y.mean()
    # calculate the integration result
    int_res = y_ave * 2


    print(int_res)
