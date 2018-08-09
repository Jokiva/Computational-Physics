from particle import RandomParticle
import numpy as np
import matplotlib.pyplot as plt
from time import time


t0 = time()

num_of_paths = (50, 500, 5000)
max_num_of_collisions = 1000

particle = RandomParticle(1)

rms = np.zeros((3, max_num_of_collisions))
for n in range(3):
    path = num_of_paths[n]
    data = np.zeros((path, max_num_of_collisions))
    for i in range(path):
        particle.reset()
        for j in range(max_num_of_collisions):
            data[i, j] = particle.displacement
            particle._RandomParticle__next()
            
    rms[n] = np.sqrt((data * data / path).sum(0))

print(time() -t0, 's elapsed')

# save the results
np.savetxt('rms_1a.txt', rms)

"""
x = np.linspace(0, 1000)
y = np.sqrt(x)

plt.figure()
for n in range(3):
    l = str(num_of_paths[n]) + ' paths' 
    plt.scatter(list(range(1000)), rms[n], marker='+', label=l)
plt.plot(x, y)

plt.legend()
plt.grid()
plt.show()
"""