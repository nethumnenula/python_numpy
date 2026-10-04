import numpy as np

# summarize data and typically return a single value

array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(np.sum(array))
print(np.mean(array))
print(np.std(array)) # Standard Deviation
print(np.var(array)) # variants = sqr of std
print(np.min(array))
print(np.max(array))
print(np.argmin(array)) # position of min value
print(np.argmax(array)) # position of max value

# summing all columns or rows it's either 0(for columns) or 1(for rows)
print(np.sum(array, axis=0))
print(np.sum(array, axis=1))
