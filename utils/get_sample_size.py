import math


def get_sample_size(z, p, e, N=None):
    """
    Get sample size

    :param z: The confidence level
    :param p: The estimated proportion
    :param e: The margin of error
    :param N: The population size
    :return: Sample size
    """
    # Infinite population
    n = (z**2 * p * (1 - p)) / e**2

    # Finite population
    if N:
        n = n / (1 + (n - 1) / N)

    return math.ceil(n)
