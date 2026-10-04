import numpy as np

# 0 DIMENSION
array1 = np.array('A')
print(array1.ndim) #  of dimensions

# 1 DIMENSION
array2 = np.array(['A', 'B', 'C'])
print(array2.ndim)

# 2 DIMENSION
array3 = np.array([['A', 'B', 'C'],
                   ['A', 'B', 'C'],
                   ['A', 'B', 'C'],
                   ['A', 'B', 'C']])
print(array3.ndim)

# 3 DIMENSION
array4 = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                   [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                   [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '_']]])
#print(array4.ndim)

#print(array4.shape)

#print(array4[0, 2, 2])

word = array4[0, 0, 0] + array4[2, 0, 0] + array4[2, 0, 1]
print(word)