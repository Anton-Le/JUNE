import numpy as np
import random
import time
# This module implements random number generator
# classes and helper functions.
# All RNGs are derived from Python's default `random` module
#

class BaseRNG(random.Random):
    # Default functions required for a derived class
    # to serve as an RNG
    def __init__(self, seed=None):
        """
        Constructor of the RNG object.
        Each pseudo or quasi random number generator requires a `seed`.
        """
        if seed is None:
            seed = time.time_ns()
        self.seed = seed
        super.seed(seed)
    def random():
        return super.random()
    def getstate(self):
        return super.getstate()
    def setstate(self, state):
        super.setstate(state)
    def getrandbits(self, k:int):
        super.getrandbits(k)
    def randbytes(self, n:int):
        return super.randbytes(n)
    # extension of `random` functions beyond scalars
    def uniform(self, a, b, size=1):
        assert size >= 1, "Number of elements must me >0"
        return [ super.uniform(a,b) for i in range(size) ] if size>1 else super.uniform(a,b)
    def choice(self, items, counts=1):
        assert counts >= 1, "Number of items to be chosen must be >= 1"
        assert len(items) >= counts, "Insufficient number of elements!"
        return super.choice(items) if counts==1 else super.choices( items, counts );

# Define a JUNE specific RNG class
# that will allow us to swap and re-seed 
# NumPy's bit generators
# 


defaultSeed = 42
#rng = BaseRNG( seed=defaultSeed )

rng = np.random.Generator( np.random.MT19937(seed=defaultSeed) )
