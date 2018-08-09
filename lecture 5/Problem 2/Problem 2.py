#!/home/jzhong/.anaconda3/bin/python

# import pacages
import numpy as np
import matplotlib.pyplot as plt

# the equation to be solved
f = lambda x: 4 * np.cos(x) - np.exp(x)

# this function returns 
# the derivative of f at x=x0
# with step epsilon / 100
# def deri(f, x0, delta):
#     return (f(x0+delta) - f(x0)) / delta

def hybFind(f, l, u, epsilon=1e-9, maxIt=500):
    xCurr = 0
    xLast = 0
    xl = l
    xu = u

    if xl == xu:
        print('the interval length should be longer than zero')
        return
    if f(xl) * f(xu) > 0:
        print('no root in the given interval')
        return
    else:
        # init xs
        if np.abs(f(xl)) < np.abs(f(xu)):
            xCurr = xl
            xLast = xu
        else:
            xCurr = xu
            xLast = xl

    # the counter
    cnt = 0

    def deri(f, x0, delta):
        return (f(x0+delta) - f(x0)) / delta

    while (np.abs(xCurr - xLast) > epsilon) & (cnt <= maxIt):
        # remember the last x
        xLast = xCurr

        # perform a NR
        xCurr = xCurr - f(xCurr) / deri(f, xCurr, epsilon/1000)

        # if this is a bad iteration
        # perform bisection
        if (xCurr < xl) | (xCurr > xu):
            xCurr = 0.5 * (xl + xu)
        
        # complete a round of iteration
        cnt += 1

        # prepare the next bracket
        xm = 0.5 * (xl + xu)
        if f(xl) * f(xm) < 0:
            xu = xm
        elif f(xu) * f(xm) < 0:
            xl = xm
        # else:
        #     print('the root is ',xm)
        #     print('exact root after',cnt, 'iterations')

    print('the root is',xCurr)
    print('after',cnt, 'iterations')
    print('precision:', np.abs(xCurr - xLast))
    return xCurr

hybFind(f, 0, 2)
