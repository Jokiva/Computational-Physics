import numpy as np
import matplotlib.pyplot as plt
from fitting import *

# data of the decay
time = np.array([0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165])
numbers = np.array([106, 80, 98, 75, 74, 73, 49, 38, 37, 22, 20, 19])
log_numbers = np.log10(numbers)

coeffs = linear_fit(time, log_numbers)
x = np.linspace(time.min(), time.max())
y = evaluate_linear_result(x, coeffs)
print(coeffs)

plt.figure()
plt.scatter(time, log_numbers, color='r')
plt.plot(x, y)
plt.grid()
plt.xlabel('$t$')
plt.ylabel('$N$')
plt.show()
