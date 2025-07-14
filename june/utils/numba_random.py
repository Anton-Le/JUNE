"""
A few numbaised useful functions for random sampling.
"""
from numba import jit
from june.utils.rng import rng
import numpy as np




#@jit(nopython=True)
def random_choice_numba_kernel(arr, prob, random_number):
    return arr[np.searchsorted(np.cumsum(prob), random_number, side="right")]

def random_choice_numba(arr, prob):
    """
    Fast implementation of np.random.choice
    """
    random_number = rng.random()
    return random_choice_numba_kernel(arr, prob, random_number)
