import numpy as np
import matplotlib.pyplot as plt

# codes for brent solver
def brent_solver(f, xs, epsilon=1e-9, max_it=500):
    # check if invalid data is inputed
    if len(xs) != 2:
        raise ValueError("xs must contain two initial value bracketing a root")
    elif (f(xs[0]) * f(xs[1]) > 0):
        raise ValueError("the two initial values must braceking a root")
    
    # if data is valid, make a copy of it
    # also initialization
    a = xs[0]
    b = xs[1]
    c = a
    
    fa = f(a)
    fb = f(b)
    fc = fa
    
    e = d = b - a
    
    p = q = s = 0
    cnt = 0
    
    # start interation
    # sentinel will mark if we will continue the iteration
    # from the accracy and steps o iteration
    conti_iter = True
    while conti_iter:
        # if c is a better approximation than b 
        # exchange the value
        if np.abs(fc) < np.abs(fb):
            a = b
            b = c
            c = a
            
            fa = fb
            fb = fc
            fc = fa
            
        
        # calculate the midpoint relative to b
        xm = 0.5 * (c - b)
        # check if the midpoint can be taken as a root
        if (np.abs(xm) < epsilon) or (fb == 0):
            conti_iter = False
        
        # check step of iteration
        if cnt > max_it:
            conti_iter = False
            
        # use bisection if the previous step width is too small
        # or the last step did not improve
        if (np.abs(e) < epsilon) or (np.abs(fa) <= np.abs(fb)):
            e = d = xm
        # otherwise we will use the interpolation method
        else:
            # only secant is proper
            if a == c:
                p = 2 * xm * fb / fa
                q = (fb - fa) / fa
            # muller is proper
            else:
                p = 2 * xm * fb * (fa - fb) / fc / fc - (b - a) * fb * (fb - fc) / (fa * fc)
                q = (fa / fc - 1) * (fb / fc - 1) * (fb / fa - 1)
                
        # make p positive
        if p > 0:
            q = -q
        else:
            p = -p
        
        # update previous step size
        s = e
        e = d
        
        # use interpolation if possible
        # or we use bisection
        if (2 * p < 3 * xm * q - np.abs(epsilon * q)) and (p < np.abs(0.5 * s * q)):
            d = p / q
        else:
            e = d = xm
        a = b
        fa = fb
        
        if np.abs(d) > epsilon:
            b = b + d
        else:
            b = b + np.sign(xm) * epsilon
            
        # calculate ew function value
        fb = f(b)
        # be sure to bracket the root 
        if fb * fc > 0:
            c = a
            fc = fa
            
            e = b - a
            d = e
            
        cnt += 1
        
    return [b, cnt]


    # sixth order lengendre polynomial
def f(x):
    return 924 * x ** 6 - 2772 * x ** 5 + 3150 * x ** 4 - 1680 * x ** 3 + 420 * x ** 2 - 42 * x + 1


# sketch it
x = np.linspace(0, 1, num=1000)
plt.figure()
plt.plot(x, f(x))
plt.grid()
plt.show()
del x

# global finding
x = np.linspace(0, 1)
x = list(x)

for i in range(len(x) - 1):
    try:
        root, step = brent_solver(f, [x[i], x[i+1]])
        print(root)
    except ValueError:
        i += 1