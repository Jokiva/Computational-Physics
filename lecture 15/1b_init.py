from particle import MoreRandomParticle
import numpy as np
import matplotlib.pyplot as plt


# num_of_paths = (50, 500, 5000)
# deltas = (0, 0.5, 0.9)
num_of_deltas = 10
deltas = [0.1 * i for i in range(num_of_deltas)]
num_of_paths = 5000
max_num_of_collisions = 1000


rms = np.zeros((num_of_deltas, max_num_of_collisions))
for n in range(num_of_deltas):
    # path = num_of_paths[n]
    de = deltas[n]
    particle = MoreRandomParticle(1, delta=de)
    data = np.zeros((num_of_paths, max_num_of_collisions))
    for i in range(num_of_paths):
        particle.reset()
        for j in range(max_num_of_collisions):
            data[i, j] = particle.displacement
            particle._MoreRandomParticle__next()
            
    rms[n] = np.sqrt((data * data / num_of_paths).sum(0))
    
    del particle

# save the results
np.savetxt('rms_1b.txt', rms)

"""
x = np.linspace(0, 1000)
y = np.sqrt(x)

plt.figure()
for n in range(3):
    l = str(deltas[n]) 
    plt.scatter(list(range(1000)), rms[n], marker='+', label=l)
plt.plot(x, y)

plt.legend()
plt.grid()
plt.show()
"""
