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

