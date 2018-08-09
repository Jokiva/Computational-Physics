import numpy as np
import matplotlib.pyplot as plt
from interpolation import LagrangeInt


# raw data
voltage = [-1.00, 0.00, 1.27, 2.55, 3.82, 4.92, 5.02]
current = [-14.58, 0.00, 0.00, 0.00, 0.00, 0.88, 11.17]

inter = LagrangeInt(voltage, current)
v = np.linspace(min(voltage), max(voltage))
i = inter.inter(v)

plt.figure()
plt.plot(v, i)
plt.scatter(voltage, current, c='r')
plt.grid()
plt.show()