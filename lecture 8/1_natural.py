# import custom packages
from cubic_spline import natural_cubic_spline, evaluate
import matplotlib.pyplot as plt


# raw data
voltage = [-1.00, 0.00, 1.27, 2.55, 3.82, 4.92, 5.02]
current = [-14.58, 0.00, 0.00, 0.00, 0.00, 0.88, 11.17]
n = len(voltage) - 1


splines = natural_cubic_spline(n, voltage, current)
x, y = evaluate(voltage, current, splines)


plt.figure()
plt.title('Natural Cubic Spline')
plt.scatter(voltage, current, c='r')
plt.plot(x, y)
plt.grid()
plt.xlabel('voltage')
plt.ylabel('current')
plt.show()
