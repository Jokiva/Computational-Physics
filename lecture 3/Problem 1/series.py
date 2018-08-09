#!/home/jzhong/.anaconda3/bin/python

def sumUp():
    """sum up to 50000"""
    s = 0.0
    for n in range(1, 500000 + 1):
        s += (-1) ** (n - 1) / (2 * n - 1)
    
    return s

def sumDown():
    """sum down to 1"""
    s = 0.0
    for n in range(500000, 0, -1):
        s += (-1) ** (n - 1) / (2 * n - 1)
    
    return s

if __name__=='__main__':
    u = sumUp()
    d = sumDown()
    diff = u - d
    print('up to 500000:', u)
    print('down to 1:', d)

    print('the difference is:', diff)