import numpy as np

class LinearEq():
    """This class contains several methods for solving system of linear equation
    Enter the n*n coefficient matrix and the constant vector
    The matrix shoud be two dimensional array and the vector one dimensional
    """
    def __init__(self, coefficient, vector):
        self.n = coefficient.shape[0]
        self.A = np.ones((coefficient.shape[0], coefficient.shape[1] + 1)) + 0.0 # initialize the matrix
        self.A[:, :self.n] = coefficient.copy()
        self.A[:, self.A.shape[1] - 1] = vector  + 0.0# assign the vector to the last column
        
    def guass(self):
        """Gauss elimination, return the solve vector"""
        # elimination phase
        for i in range(self.n):
            for j in range(i + 1, self.n):
                self.A[j] = self.A[j] - self.A[i] * self.A[j, i] / self.A[i, i]
                
        # backward substitution
        self.A[self.n - 1, self.n] = self.A[self.n - 1, self.n] / self.A[self.n - 1, self.n - 1] # last element
        for i in range(self.n - 2, -1, -1):
            self.A[i, self.n] = (self.A[i, self.n] - self.A[i, i + 1: self.n - 1].dot(self.A[i + 1: self.n - 1, self.n])) / self.A[i, i]
        return self.A[:, self.n].copy()

    
# example for testing
A = np.array([[2, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
b = np.array([2, 2, 3, 4])

eq = LinearEq(A, b)
eq.guass()
