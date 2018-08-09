import numpy as np
import matplotlib.pyplot as plt
from interpolation import LagrangeInt

# the function to be interpolated
def f(x):
    return x * np.sin(2 * np.pi * x + 1)


# plot on individual figures
num_of_nodes = [6, 7, 9, 17, 19, 21]
for node in num_of_nodes:
    # create sampled data for interpolation first
    x_data = np.linspace(-1, 1, num=node)
    y_data = f(x_data)
    
    # create a container for generating the result of interpolations
    x = np.linspace(-1, 1, num=1000)
    
    # create an interpoaltion object
    inter_session = LagrangeInt(x_data, y_data)
    # get the interpolation result
    y = inter_session.inter(x)
    
    # generate title for each figure
    func_name = r'$f(x) = x \sin(2 \pi x + 1)$'
    title = 'Interpolate ' + func_name + ' with '+ str(node) + ' nodes'
    
    # generate orinigal function
    y_ori = f(x)
    
    plt.figure()
    # interpolation
    plt.plot(x, y, label='interpolation')
    # node
    plt.scatter(x_data, y_data, c='r')
    # original 
    plt.plot(x, y_ori, label='original')
    
    plt.ylim(-1.25, 1.25)
    plt.title(title)
    plt.legend(loc=1)
    plt.grid()
    
plt.show()


# plot on one figure
num_of_nodes = [6, 7, 9, 17, 19, 21]

plt.figure()
for node in num_of_nodes:
    # create sampled data for interpolation first
    x_data = np.linspace(-1, 1, num=node)
    y_data = f(x_data)
    
    # create a container for generating the result of interpolations
    x = np.linspace(-1, 1, num=1000)
    
    # create an interpoaltion object
    inter_session = LagrangeInt(x_data, y_data)
    # get the interpolation result
    y = inter_session.inter(x)
    
    # generate title for each figure
    func_name = r'$f(x) = x \sin(2 \pi x + 1)$'
    title = 'Interpolate ' + func_name + ' with various nodes'
    
    # generate orinigal function
    y_ori = f(x)
    
    # interpolation
    plt.plot(x, y, label=str(node) + ' nodes')
    # node
    # plt.scatter(x_data, y_data, c='r')
        
    plt.ylim(-1.25, 1.25)
    plt.title(title)

# original 
x = np.linspace(-1, 1, num=1000)
plt.plot(x, y_ori, label='original')
plt.xlim(-1, 1.75)
plt.legend(loc=1)
plt.grid()    
plt.show()

