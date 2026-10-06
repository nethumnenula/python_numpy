import numpy as np

# if seed was set to be 1, the generated numbers will be the same

rng = np.random.default_rng(seed=1)

print(rng.integers(low=1, high=700, size=(3, 3)))

# floating point numbers
# default values will be 0 and 1
np.random.seed(seed=1)
print(np.random.uniform(low=-1, high=1, size=(3,2)))