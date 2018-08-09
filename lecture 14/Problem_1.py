# import packages
import numpy as np
import matplotlib.pyplot as plt


# defination od f integrand
def f(x):
    return np.exp(x)


if __name__ == '__main__':
    # constants in the problem
    # number of integrations
    num_of_int = 10000
    # samples per integration
    samp_per_int = 100000


    # container of integration result
    int_res_container = np.zeros(num_of_int)


    # start the integration
    for i in range(num_of_int):

        # sample the function from a certain interval
        x_samples = np.random.uniform(0, 1, size=samp_per_int);
        y_samples = f(x_samples)

        y_ave = y_samples.mean()
        int_res = y_ave * 1
        int_res_container[i] = int_res

    
    # some analysis of the data
    sample_exp = int_res_container.mean()
    sample_std = int_res_container.std()
    # the sample probability density function
    def sample_pdf(x):
        return 1 / (np.sqrt(2 * np.pi) * sample_std) * np.exp(- (x - sample_exp) ** 2 / 2 / sample_std ** 2)

    x = np.linspace(int_res_container.min(), int_res_container.max(), num_of_int)
    y = sample_pdf(x)


    print(int_res_container)
    print(sample_exp)
    print(sample_std)
    # make a histogram of the integration result
    plt.figure()
    # the histogram
    plt.hist(int_res_container,
             bins=50,
             normed=True)
    # the sample pdf
    # plt.plot(x, y)

    # annotate the plot
    plt.grid()
    plt.show()
