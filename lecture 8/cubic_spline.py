"""cubic_spline.py
Implementations of the natural (and maybe clamped) cubic spline algorithms
"""
from typing import List, Tuple


def natural_cubic_spline(n, x, a):
    b = [0.0] * (n + 1)
    c = [0.0] * (n + 1)
    d = [0.0] * (n + 1)
    u = [0.0] * n
    l = [0.0] * (n + 1)
    z = [0.0] * (n + 1)

    # step 1
    h = [x[i + 1] - x[i] for i in range(n)]

    def calculate_matrix_entry(i):
        return (3.0 / h[i]) * (a[i+1] - a[i]) - (3.0/h[i-1]) * (a[i] - a[i-1])

    # step 2
    alpha = [calculate_matrix_entry(i) for i in range(1, n)]
    l[0] = 1
    u[0] = 0
    z[0] = 0

    for i in range(1, n):
        l[i] = 2 * (x[i+1] - x[i-1]) - (h[i-1] * u[i-1])
        u[i] = h[i]/l[i]
        z[i] = (alpha[i-1] - h[i-1] * z[i-1]) / l[i]

    l[n] = 1
    z[n] = 0
    c[n] = 0

    for j in range(n-1, -1, -1):
        c[j] = z[j] - u[j]*c[j+1]
        b[j] = (a[j+1] - a[j])/h[j] - h[j]*(c[j+1] + 2*c[j])/3
        d[j] = (c[j+1] - c[j]) / (3*h[j])

    from utility import cleanup_list
    a = cleanup_list(a)
    b = cleanup_list(b)
    c = cleanup_list(c)
    d = cleanup_list(d)

    return list(zip(a[:-1], b[:-1], c[:-1], d[:-1]))


def clamped_cubic_spline(n: int, x: List[float], a: List[float], primes: Tuple[float, float]):
    b = [0.0] * (n + 1)
    c = [0.0] * (n + 1)
    d = [0.0] * (n + 1)
    u = [0.0] * n
    l = [0.0] * (n + 1)
    z = [0.0] * (n + 1)
    alpha = [0.0] * (n + 1)

    fpo, fpn = primes
    h = [x[i+1] - x[i] for i in range(n)]
    alpha[0] = 3*(a[1] - a[0]) / h[0] - 3 * fpo
    alpha[n] = 3 * fpn - 3 * (a[-1] - a[-2])/h[-1]

    def calculate_alpha_entry(i: int):
        alpha[i] = (3 / h[i]) * (a[i+1] - a[i]) - (3 / h[i-1]) * (a[i] - a[i-1])

    for i in range(1, n):
        calculate_alpha_entry(i)

    l[0] = 2 * h[0]
    u[0] = 0.5
    z[0] = alpha[0] / l[0]

    for i in range(1, n):
        l[i] = 2 * (x[i+1] - x[i-1]) - h[i-1] * u[i-1]
        u[i] = h[i]/l[i]
        z[i] = (alpha[i] - h[i-1] * z[i-1]) / l[i]

    l[n] = h[n-1] * (2 - u[n-1])
    z[n] = (alpha[n] - h[n-1] * z[n-1]) / l[n]
    c[n] = z[n]

    for j in range(n - 1, -1, -1):
        c[j] = z[j] - u[j]*c[j+1]
        b[j] = (a[j+1] - a[j]) / h[j] - h[j] * (c[j+1] + 2 * c[j]) / 3
        d[j] = (c[j+1] - c[j]) / (3 * h[j])

    from utility import cleanup_list
    a = cleanup_list(a)
    b = cleanup_list(b)
    c = cleanup_list(c)
    d = cleanup_list(d)

    for j in range(n):
        yield (a[j], b[j], c[j], d[j])


def spline_function(a, b, c, d, x0, x):
    h = x - x0
    return a + b * h + c * h ** 2 + d * h ** 3


def evaluate(x_data, y_data, splines, panels=100):
    n = len(x_data) - 1

    # splines = natural_cubic_spline(n, x_points, y_points)
    curve_x = []
    curve_y = []
    # subinterval = 4
    for idx, spline in enumerate(splines):
        x0, x1 = x_data[idx], x_data[idx + 1]
        diff = round((x1-x0) / panels, 5)
        curve_x.append(x0)
        curve_y.append(y_data[idx])
        for i in range(panels):
            curve_x.append(round(x0 + diff, 5))
            result = spline_function(*spline, x0, x0 + diff)
            curve_y.append(round(result, 5))

    curve_x.append(x_data[-1])
    curve_y.append(y_data[-1])

    return curve_x, curve_y


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    x_points = [
        0.9,
        1.3,
        1.9,
        2.1,
        2.6,
        3.0,
        3.9,
        4.4,
        4.7,
        5.0,
        6.0,
        7.0,
        8.0,
        9.2,
        10.5,
        11.3,
        11.6,
        12.0,
        12.6,
        13.0,
        13.3,
    ]
    y_points = [
        1.3,
        1.5,
        1.85,
        2.1,
        2.6,
        2.7,
        2.4,
        2.15,
        2.05,
        2.1,
        2.25,
        2.3,
        2.25,
        1.95,
        1.4,
        0.9,
        0.7,
        0.6,
        0.5,
        0.4,
        0.25,
    ]
    n = len(x_points) - 1

    splines = natural_cubic_spline(n, x_points, y_points)
    graph_x = []
    graph = []
    subinterval = 400
    for idx, spline in enumerate(splines):
        x0, x1 = x_points[idx], x_points[idx + 1]
        diff = round((x1-x0) / subinterval, 5)
        graph_x.append(x0)
        graph.append(y_points[idx])
        for i in range(subinterval):
            graph_x.append(round(x0 + diff, 5))
            result = spline_function(*spline, x0, x0 + diff)
            graph.append(round(result, 5))

    graph_x.append(x_points[-1])
    graph.append(y_points[-1])

    # plt.plot(x_points, y_points, 'bo')
    plt.plot(graph_x, graph, 'b-')

    # plt.axis([0, 14, -6, 4])
    plt.show()
