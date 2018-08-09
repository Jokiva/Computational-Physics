def forward_diff(f, x0, h):
    return (f(x0 + h) - f(x0)) / h


def central_diff(f, x0, h):
    return (f(x0 + h / 2) - f(x0 - h / 2)) / h

if __name__ == '__main__':
    def f(x):
        return x ** 2 + x - 1

    def g(x):
        return 2 * x + 1

    f_diff = forward_diff(f, 3, 0.1)
    c_diff = central_diff(f, 3, 0.1)
    analytical = g(3)

    f_err = abs(f_diff - analytical) / analytical
    c_err = abs(c_diff - analytical) / analytical


    print('analytical result:', analytical)
    print()
    print('forward difference:', f_diff)
    print('error:', f_err)
    print()
    print('central difference:', c_diff)
    print('error:', c_err)
    
