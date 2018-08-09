# import custom packages
from cubic_spline import evaluate, clamped_cubic_spline
import matplotlib.pyplot as plt


# raw data
voltage = [-1.00, 0.00, 1.27, 2.55, 3.82, 4.92, 5.02]
current = [-14.58, 0.00, 0.00, 0.00, 0.00, 0.88, 11.17]
n = len(voltage) - 1


spliles = clamped_cubic_spline(n, voltage, current, (1.0, 1.0))
x, y = evaluate(voltage, current, spliles)


plt.figure()
plt.title('Clamped Cubic Spline')
plt.scatter(voltage, current, c='r')
plt.plot(x, y)
plt.grid()
plt.xlabel('voltage')
plt.ylabel('current')
plt.show()
