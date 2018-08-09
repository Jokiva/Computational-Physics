# import packages
import numpy as np
import matplotlib.pyplot as plt


# the amount of shift up
verti_dev = 3

# the modified integrand
def f_prime(x):
    return 2 * np.sin(2 * np.sqrt(np.pi ** 2 - x ** 2)) + verti_dev


if __name__ == '__main__':
    # test block
    """
    x = np.linspace(0, np.pi)
    y = f_prime(x)

    plt.plot(x, y)
    plt.show()
    """
    
    # random sampling
    num_of_samp = 100000
    x = np.random.uniform(0, np.pi, num_of_samp)
    y = np.random.uniform(0, 6, num_of_samp)

    # containers for different types of dots
    above = []
    below = []
    
    # count the scuccess
    success = 0
    for i in range(num_of_samp):
        if y[i] < f_prime(x[i]):
            below.append((x[i], y[i]))
            success += 1
        else:
            above.append([x[i], y[i]])

    # calculate the probability
    p = success / num_of_samp
    # the modified area
    area = p * 6 * (np.pi - 0)
    # the actual area
    area = area - verti_dev * (np.pi - 0)

    # print the integration result
    print(area)
    

    # some maniplation on the data
    above = np.array(above)
    below = np.array(below)
    # the threshold of dots
    thresh_of_dots = 3000
    # the annotate of plot
    anno = r'$\int_{0}^{\pi}{2 \sin (2 \sqrt{\pi^2 - x^2})} \approx$' + '${}$'.format(area)
    plt.figure()
    # plot the fucntion
    x_spc = np.linspace(0, np.pi, num_of_samp)
    plt.plot(x_spc, f_prime(x_spc) - verti_dev,
             c='c',
             linewidth=5)

    # plot the dots
    # plt.scatter(x, y)
    # above
    """
    for x_pos, y_pos in above:
        plt.scatter(x_pos, y_pos - verti_dev, c='b')
    """
    plt.scatter(above[:thresh_of_dots, 0], above[:thresh_of_dots, 1] - verti_dev, c='b', marker='+')
    # below
    """
    for x_pos, y_pos in below:
        plt.scatter(x_pos, y_pos - verti_dev, c='r')
    """
    plt.scatter(below[:thresh_of_dots, 0], below[:thresh_of_dots, 1] - verti_dev, c='r', marker='+')
    plt.title(anno)
    plt.grid()
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.show()
