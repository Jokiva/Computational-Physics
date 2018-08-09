# import custom packages
from cubic_spline import clamped_cubic_spline, evaluate
import matplotlib.pyplot as plt
import numpy as np


num_of_nodes = [6, 7, 9, 17, 19, 21]

plt.figure()
plt.title('Natural Cubic Spline')
for node in num_of_nodes:
    # create sampled data for interpolation first
    x_data = np.linspace(-1, 1, num=node)
    y_data = f(x_data)
    curve_name = str(node) + ' nodes'

    x_data = list(x_data)
    y_data = list(y_data)
    
    n = len(x_data) - 1
    splines = clamped_cubic_spline(n, x_data, y_data, (-2, 6))
    x, y = evaluate(x_data, y_data, splines)
    plt.plot(x, y, label=curve_name)
plt.grid()
plt.legend()
plt.show()
