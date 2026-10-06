import numpy as np

rng = np.random.default_rng()

array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)
print(array)

fruits = np.array(["orange", "banana", "grapes", "orange"])
fruit = rng.choice(fruits, size=(3,3))
print(fruit)