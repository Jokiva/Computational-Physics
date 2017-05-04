# ## Neville’s Method
# 
# Newton's method of interpolation involves two steps
# 1. Computation of the coefficients
# 2. Evaluation of the polynomial
# 
# If only one point is to be interpolated, a method that computes the interpolant in a single step,
# such as **Neville's algorithm**, is a better choice.

# import modules needed
import numpy as np
import matplotlib.pyplot as plt

class NevilleInt():
    def __init__(self, xData, yData):
        self.xData = xData
        self.yData = yData
        self.n = xData.shape[0] # remember the length of the rows/ columns
        
        self.p = np.zeros((self.n, self.n), dtype=float) # initialize the matrix for interpolation
        for i in range(self.n): # load the y data to the diagnol
            self.p[i, i] = self.yData[i]
            
    def inter(self, x): # interpolation
        for i in range(1, self.n):
            for j in range(self.n - i):
                self.p[j, j + i] = ((x - self.xData[j + i]) * self.p[j, j + i - 1] - (x - self.xData[j]) * self.p[j + 1, j + i]) / (self.xData[j] - self.xData[j + i])
        return self.p[0, self.n - 1]
        

# an example
x = np.arange(0.1, 0.6, 0.1)
y = np.array([-1.6228, -0.8218, -0.3027, 0.1048, 0.4542])

p = NevilleInt(x, y)
p.inter(0.15)
