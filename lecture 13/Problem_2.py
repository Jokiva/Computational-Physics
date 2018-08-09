from random import uniform
from multiprocessing.pool import Pool
from time import time


def estimate_nbr_points_in_quarter_circle(nbr_estimate):
    nbr_trials_in_quarter_unit_circle = 0

    for step in range(int(nbr_estimate)):
        x = uniform(0, 1)
        y = uniform(0, 1)

        is_in_unit_circle = x * x + y * y <= 1
        nbr_trials_in_quarter_unit_circle += is_in_unit_circle

    return nbr_trials_in_quarter_unit_circle


if __name__ == "__main__":
    nbr_sample_in_total = 1e8
    nbr_parallel_blocks = 3
    # p = pool(process=nbr_parallel_blocks)
    pool = Pool(processes=nbr_parallel_blocks)

    nbr_sample_per_worker = nbr_sample_in_total / nbr_parallel_blocks
    print('making {} samples per worker'.format(nbr_sample_per_worker))

    nbr_trials_per_process = [nbr_sample_per_worker] * nbr_parallel_blocks

    t0 = time()

    nbr_in_unit_circles = pool.map(estimate_nbr_points_in_quarter_circle, nbr_trials_per_process)
    pi_estimate = sum(nbr_in_unit_circles) * 4 / nbr_sample_in_total

    print('estimated pi:',pi_estimate)
    print('time elapesed:', time() - t0)
