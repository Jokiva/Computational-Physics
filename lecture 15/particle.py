# import packeges
import numpy as np


class RandomParticle(object):
    """base class for randomly wallking particles"""

    # constructor
    def __init__(self, mean_free_path, start=(0, 0, 0)):
        """
        init the object by assigning the mean free path and starting position
        the starting position is set to origin by default
        """
        self.__mean_free_path = mean_free_path
        self.__start = start

        # the empty list for remembering the path
        self.__positions = []
        # put the first element in the tail
        self.__positions.append(self.__start)


    def __next(self):
        """
        move the particle forward once
        """
        phi = np.random.uniform(0, 2 * np.pi)
        cos_theta = np.random.uniform(-1, 1)
        sin_theta = np.sqrt(1 - cos_theta ** 2)

        # copy the current position
        curr_pos = self.__positions[-1]

        # calculate the next position
        next_x = curr_pos[0] + self.__mean_free_path * sin_theta * np.cos(phi)
        next_y = curr_pos[1] + self.__mean_free_path * sin_theta * np.sin(phi)
        next_z = curr_pos[2] + self.__mean_free_path * cos_theta

        # append the new list to the path
        self.__positions.append((next_x, next_y, next_z))


    def evolve(self, steps=100):
        """
        simulate the evolution of particle for certain steps
        """
        for i in range(steps):
            self.__next()


    def reset(self):
        """
        clear the path and move the particle to the primarily set position
        """
        self.__positions.clear()
        self.__positions.append(self.__start)


    @property
    def path(self):
        """
        the path of the particle after the evolution
        """
        return np.array(self.__positions)


    @property
    def displacement(self):
        """
        the displacement from start to end
        """
        init = self.path[0]
        last = self.path[-1]
        disp = last - init
        return np.sqrt((disp * disp).sum())


class MoreRandomParticle(RandomParticle):
    def __init__(self, mean_free_path, start = (0, 0, 0), delta=0.1):
        """
        init the object by assigning the mean free path and starting position
        the starting position is set to origin by default
        """
        self.delta = delta
        return super().__init__(mean_free_path, start)

    """
    the step for each evolution is random
    derived from RamdomParticle
    """
    def __next(self):
        """
        move the particle forward once
        """
        phi = np.random.uniform(0, 2 * np.pi)
        cos_theta = np.random.uniform(-1, 1)
        sin_theta = np.sqrt(1 - cos_theta ** 2)

        # actual free path
        actual_path = self._RandomParticle__mean_free_path * np.random.uniform(1 - self.delta, 1 + self.delta)

        # copy the current position
        curr_pos = self._RandomParticle__positions[-1]
        # add random fluctuation to the step

        # calculate the next position
        next_x = curr_pos[0] + actual_path * sin_theta * np.cos(phi)
        next_y = curr_pos[1] + actual_path * sin_theta * np.sin(phi)
        next_z = curr_pos[2] + actual_path * cos_theta

        # append the new list to the path
        self._RandomParticle__positions.append((next_x, next_y, next_z))


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    from time import time


    t0 = time()

    particle = MoreRandomParticle(1, delta=0.5)
    particle.evolve(1000)
    path = particle.path
    # print(path)
    print(particle.displacement)

    print(time() -t0, 's elapsed')

    # plot the path
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(path[:, 0], path[:, 1], path[:, 2])
    # ax.scatter(path[:, 0], path[:, 1], path[:, 2], c='r')
    plt.show()

    particle.reset()
    print(particle.displacement)
    