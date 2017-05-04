
# coding: utf-8

# # Polynomial Interpolation
# 
# Polynormial interpolation tries to find a (n-1) degree polynormial passes through n points
# 
# Polynormial interpolation is a globel method, paying **less attention** to the local properties. If there are many data pointsr ranging widely, polynormial may **not** be a good choice. 
# 
# Example: property of a material under different temperatures

# ## Lagrange’s Method


# import modules needed
import numpy as np
import matplotlib.pyplot as plt


class LagrangeInt():
    def __init__(self, xData, yData): # initialize all the parameter
        self.xData = xData
        self.yData = yData
        self.length = len(xData)
    
    def l(self, x, i, xData):
        """
        return the value of cardinal functions
    x is the point where the base function is evaluated,
    i is the order and xData is obvious
    """
        t1, t2 = 1, 1
        for j in range(self.length):
            if j != i:
                t1 *= x - self.xData[j]
                t2 *= self.xData[i] - self.xData[j]
        return t1 / t2
    
    def inter(self, x):
        """return the interpolated resualt on interval x
        """
        s = 0
        for i in range(self.length):
            s += self.l(x, i, self.xData) * self.yData[i]
        return s


# put it to test
# votage and current
x = np.array([-1, 0, 0.27, 2.55, 3.82, 4.92, 5.02])
y = np.array([-14.58, 0, 0, 0, 0, 0.88, 11.17])

p = LagrangeInt(x, y)
x1 = np.linspace(-1, 5.02)
y1 = p.inter(x1)
plt.scatter(x, y, color='red')
plt.plot(x1, y1)
plt.xlabel('Votage')
plt.ylabel('Current')
plt.title('Relationship between Votage and Current')
plt.grid()
plt.legend(['Experimental', 'Interpolated'], loc='best')
plt.show()


# Ei(x)
x = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
y = np.array([-1.6228, -0.8218, -0.3027, 0.1048, 0.4542])

p = LagrangeInt(x, y)
x1 = np.linspace(0.1, 0.5)
y1 = p.inter(x1)
plt.scatter(x, y, color='red')
plt.plot(x1, y1)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('The value of $Ei(x)$')
plt.grid()
plt.legend(['Discrete', 'Interpolated'], loc='best')
plt.show()
