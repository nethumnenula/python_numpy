import numpy as np

array = np.array([[ 1,  2,  3,  4],
                  [ 5,  6,  7,  8],
                  [ 9, 10, 11, 12],
                  [13, 14, 15, 16]])

# array[start:end:step] <- Subscript Operator

# ROW SELECTION
print("# ROW SELECTION")
print(array[0:4:2])
print(array[::2])
print(array[::-1])

print()

# COLUMN SELECTION
print("# COLUMN SELECTION")
print(array[0, 0])
print(array[:, 0:3])
print(array[:, 1:4])
print(array[:, ::2])
print(array[:, 1::2])
print(array[:, 1::-1])


# COMBINE ROWS AND COLUMNS
print("# COMBINE ROWS AND COLUMNS")
print(array[0:2, 0:2])
print(array[0:2, 2:])
print(array[1:3, 1:3])
print(array[2:, 0:2])
print(array[2:, 2:])