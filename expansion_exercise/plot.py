import matplotlib.pyplot as plt


x = open('x.txt').read().splitlines()
y1 = open('y1.txt').read().splitlines()
y2 = open('y2.txt').read().splitlines()
error = open('error.txt').read().splitlines()

plt.figure(num='Expansion')
plt.title('$(x-1)^7$ Expansion')
plt.xlim((0.9975, 1.0025))
plt.ylim((-1e-15, 1e-15))
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.scatter(x, y1, color='red')


plt.figure(num='Extraction')
plt.title('$(x-1)^7$ Extraction')
plt.xlim((0.9975, 1.0025))
plt.ylim((-1e-15, 1e-15))
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.scatter(x, y2, color='green')

plt.figure(num='Error')
plt.title('Relative Error')
plt.xlim((0.99, 1.01))
plt.ylim((0, 50))
plt.xlabel('$x$')
plt.ylabel('Error')
plt.scatter(x, error,color='blue')

error_n = [float(x) for x in error]
plt.figure(num='Error Histogram')
plt.title('Error Histogram')
plt.xlim((0, 1e72))
plt.xlabel('$x$')
plt.hist(error_n, bins=100, color='purple')

plt.show()
